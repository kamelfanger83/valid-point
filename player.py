import pygame
import sprites
import copy

class Player:
    def __init__(self, x, y, x_hit = 0.2, y_hit = 1):
        self.x = x
        self.y = y
        self.x_hit = x_hit
        self.y_hit = y_hit

        self.speed = 0.1
        self.crouchSpeed = 0.2

        self.direction = 0 # 0 = right, 1 = left

        self.velocity_up = 0

        self.isWalking = False
        self.isCrouching = False

        self.jump_height = 2
        self.gravity = 0.02
        self.jump_speed = 0.35

        self.doubleJumped = True

        self.walkinframe = 1
        self.thisframe = 0
        self.lwpressed = False

    def load_sprites(self, tile_size):
        # load player image, left and right
        self.stand_left = sprites.Sprite(".\sprites\\player_l.png", 1, 2, tile_size)
        self.stand_right = sprites.Sprite(".\sprites\\player_r.png", 1, 2, tile_size)

        # load crouch image, left and right
        self.crouch_left = sprites.Sprite(".\sprites\\crouch_l.png", 1, 2, tile_size)
        self.crouch_right = sprites.Sprite(".\sprites\\crouch_r.png", 1, 2, tile_size)

        # load jump image, left and right
        self.jump_left = sprites.Sprite(".\sprites\\jump_l.png", 1, 2, tile_size)
        self.jump_right = sprites.Sprite(".\sprites\\jump_r.png", 1, 2, tile_size)

        # load walk images, left and right, 1-2
        self.walk_left_1 = sprites.Sprite(".\sprites\\walk_l_1.png", 1, 2, tile_size)
        self.walk_left_2 = sprites.Sprite(".\sprites\\walk_l_2.png", 1, 2, tile_size)
        self.walk_right_1 = sprites.Sprite(".\sprites\\walk_r_1.png", 1, 2, tile_size)
        self.walk_right_2 = sprites.Sprite(".\sprites\\walk_r_2.png", 1, 2, tile_size)

        # load crouch walk images, left and right, 1-2
        self.crouch_walk_left_1 = sprites.Sprite(".\sprites\\crouch_walk_l_1.png", 1, 2, tile_size)
        self.crouch_walk_left_2 = sprites.Sprite(".\sprites\\crouch_walk_l_2.png", 1, 2, tile_size)
        self.crouch_walk_right_1 = sprites.Sprite(".\sprites\\crouch_walk_r_1.png", 1, 2, tile_size)
        self.crouch_walk_right_2 = sprites.Sprite(".\sprites\\crouch_walk_r_2.png", 1, 2, tile_size)

    def is_valid(self, grid):
        if self.isCrouching:
            if grid[int(self.x - self.x_hit)][int(self.y - self.y_hit)] == 0 and \
               grid[int(self.x + self.x_hit)][int(self.y - self.y_hit)] == 0 and \
               grid[int(self.x - self.x_hit)][int(self.y - 10**-10)] == 0 and \
               grid[int(self.x + self.x_hit)][int(self.y - 10**-10)] == 0:
                return True
        else:
            if grid[int(self.x - self.x_hit)][int(self.y - self.y_hit)] == 0 and \
               grid[int(self.x + self.x_hit)][int(self.y - self.y_hit)] == 0 and \
               grid[int(self.x - self.x_hit)][int(self.y)] == 0 and \
               grid[int(self.x + self.x_hit)][int(self.y)] == 0 and \
               grid[int(self.x - self.x_hit)][int(self.y + self.y_hit)] == 0 and \
               grid[int(self.x + self.x_hit)][int(self.y + self.y_hit)] == 0:
                return True
        return False

    def get_events(self, grid):
        # get the pressed keys
        pressed_keys = pygame.key.get_pressed()

        self.isWalking = False
        self.isCrouching = False

        nlwpressed = False
        if pressed_keys[pygame.K_w]:
            nlwpressed = True
            if self.lwpressed:
                pass
            elif not self.doubleJumped:
                self.velocity_up = 2 / 3 * self.jump_speed
                self.doubleJumped = True
            elif (grid[int(self.x - self.x_hit)][int(self.y - self.y_hit - 10**-10)] == 1 or grid[int(self.x + self.x_hit)][int(self.y - self.y_hit - 10**-10)] == 1) and self.y == int(self.y):
                self.velocity_up = self.jump_speed
                self.doubleJumped = False

        self.lwpressed = nlwpressed

        o_player = Player(self.x, self.y)
        o_player.isCrouching = self.isCrouching

        if pressed_keys[pygame.K_s]:
            self.isCrouching = True

        if pressed_keys[pygame.K_a]:
            if self.isCrouching:
                self.x -= self.crouchSpeed
            else:
                self.x -= self.speed
            self.direction = 1
            self.isWalking = True

        if pressed_keys[pygame.K_d]:
            if self.isCrouching:
                self.x += self.crouchSpeed
            else:
                self.x += self.speed
            self.direction = 0
            self.isWalking = True

        if not self.is_valid(grid):
            self.x = o_player.x
            self.y = o_player.y
            self.isCrouching = o_player.isCrouching

        o_player = Player(self.x, self.y)

        self.velocity_up -= self.gravity
        self.y += self.velocity_up

        # check if player is on the ground
        if grid[int(self.x-self.x_hit)][int(self.y - self.y_hit)] == 1 or grid[int(self.x+self.x_hit)][int(self.y - self.y_hit)] == 1:
            self.velocity_up = 0
            self.y = int(self.y) + self.y_hit
            self.doubleJumped = True

        if not self.is_valid(grid):
            self = o_player
            self.velocity_up = 0

    def draw(self, surface, camera):
        # draw the player
        if self.isCrouching:
            if self.isWalking:
                if self.walkinframe == 1:
                    if self.direction == 1:
                        self.crouch_walk_left_1.draw(surface,
                                                camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                    else:
                        self.crouch_walk_right_1.draw(surface,
                                                 camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                else:
                    if self.direction == 1:
                        self.crouch_walk_left_2.draw(surface,
                                                camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                    else:
                        self.crouch_walk_right_2.draw(surface,
                                                 camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                if self.thisframe == 10:
                    self.walkinframe = 3 - self.walkinframe
                    self.thisframe = 0
                self.thisframe += 1
            else:
                if self.direction == 1:
                    self.crouch_left.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                else:
                    self.crouch_right.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))

        elif self.isWalking:
            if self.direction == 1:
                if self.walkinframe == 1:
                    self.walk_left_1.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                else:
                    self.walk_left_2.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            else:
                if self.walkinframe == 1:
                    self.walk_right_1.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
                else:
                    self.walk_right_2.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            if self.thisframe == 10:
                self.walkinframe = 3 - self.walkinframe
                self.thisframe = 0
            self.thisframe += 1

        elif self.velocity_up != 0:
            if self.direction == 1:
                self.jump_left.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            else:
                self.jump_right.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
        else:
            if self.direction == 0:
                self.stand_right.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            else:
                self.stand_left.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))