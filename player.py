import pygame
import sprites
import object

class Player(object.Object):
    def __init__(self, x, y, x_hit = 0.2, y_hit = 0.999):
        self.x = x
        self.y = y

        self.x_hit = x_hit
        self.y_hit = y_hit
        self.hitbox = object.RectangularHitbox(x_hit, y_hit, 0.5)

        self.speed = 0.1
        self.crouchSpeed = 0.2

        self.direction = 0 # 0 = right, 1 = left

        self.velocity_up = 0

        self.isWalking = False
        self.isCrouching = False

        self.jump_height = 2
        self.gravity = 0.02
        self.jump_speed = 0.35

        self.singleJumped = False
        self.doubleJumped = False

        self.onFloor = False

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

    def get_events(self, grid):
        # get the pressed keys
        pressed_keys = pygame.key.get_pressed()

        o_x = self.x
        o_y = self.y

        self.isWalking = False
        self.onFloor = False

        nlwpressed = False
        if pressed_keys[pygame.K_w]:
            nlwpressed = True
            if self.lwpressed:
                pass
            elif not self.singleJumped:
                self.velocity_up = self.jump_speed
                self.y += self.velocity_up
                self.singleJumped = True
            elif not self.doubleJumped:
                self.velocity_up = 2 / 3 * self.jump_speed
                self.y += self.velocity_up
                self.doubleJumped = True

        if not self.is_valid(grid):
            self.x = o_x
            self.y = o_y
            self.velocity_up = 0

        o_x = self.x
        o_y = self.y

        self.lwpressed = nlwpressed

        if pressed_keys[pygame.K_s]:
            if not self.isCrouching:
                self.hitbox = object.RectangularHitbox(self.x_hit, self.y_hit/2, 0.5, 0, -self.y_hit/2)
            self.isCrouching = True
        else:
            if self.isCrouching:
                self.hitbox = object.RectangularHitbox(self.x_hit, self.y_hit, 0.5)
                self.isCrouching = False
                if not self.is_valid(grid):
                    self.hitbox = object.RectangularHitbox(self.x_hit, self.y_hit / 2, 0.5, 0, -self.y_hit / 2)
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
            self.x = o_x
            self.y = o_y

        o_x = self.x
        o_y = self.y

        self.velocity_up -= self.gravity
        self.y += self.velocity_up

        if self.on_ground(grid):
            self.onFloor = True
            self.velocity_up = 0
            self.y = int(self.y) + self.y_hit + 10**-10
            self.singleJumped = False
            self.doubleJumped = False

        if not self.is_valid(grid):
            self.x = o_x
            self.y = o_y
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

        elif not self.onFloor:
            if self.direction == 1:
                self.jump_left.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            else:
                self.jump_right.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
        else:
            if self.direction == 0:
                self.stand_right.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))
            else:
                self.stand_left.draw(surface, camera.coords_to_screen(self.x - 1 / 2, self.y + 1, surface))