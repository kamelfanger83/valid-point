import pygame
import sprites
import object
import gödi
import sand

class Player(object.Object):
    def __init__(self, x = 0, y = 0, x_hit = 0.2, y_hit = 0.85):
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

    def load(self, tile_size, bigSprite):
        # load player image, left and right
        bigSprite.load_sprite(".\\data\\img\\player_l.png", 5*self.x_hit, 2*self.y_hit, tile_size, "player_l")
        bigSprite.load_sprite(".\\data\\img\\player_r.png", 5*self.x_hit, 2*self.y_hit, tile_size, "player_r")

        # load crouch image, left and right
        bigSprite.load_sprite(".\\data\\img\\crouch_l.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_l")
        bigSprite.load_sprite(".\\data\\img\\crouch_r.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_r")

        # load jump image, left and right
        bigSprite.load_sprite(".\\data\\img\\jump_l.png", 5*self.x_hit, 2*self.y_hit, tile_size, "jump_l")
        bigSprite.load_sprite(".\\data\\img\\jump_r.png", 5*self.x_hit, 2*self.y_hit, tile_size, "jump_r")

        # load walk images, left and right, 1-2
        bigSprite.load_sprite(".\\data\\img\\walk_l_1.png", 5*self.x_hit, 2*self.y_hit, tile_size, "walk_l_1")
        bigSprite.load_sprite(".\\data\\img\\walk_l_2.png", 5*self.x_hit, 2*self.y_hit, tile_size, "walk_l_2")
        bigSprite.load_sprite(".\\data\\img\\walk_r_1.png", 5*self.x_hit, 2*self.y_hit, tile_size, "walk_r_1")
        bigSprite.load_sprite(".\\data\\img\\walk_r_2.png", 5*self.x_hit, 2*self.y_hit, tile_size, "walk_r_2")

        # load crouch walk images, left and right, 1-2
        bigSprite.load_sprite(".\\data\\img\\crouch_walk_l_1.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_walk_l_1")
        bigSprite.load_sprite(".\\data\\img\\crouch_walk_l_2.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_walk_l_2")
        bigSprite.load_sprite(".\\data\\img\\crouch_walk_r_1.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_walk_r_1")
        bigSprite.load_sprite(".\\data\\img\\crouch_walk_r_2.png", 5*self.x_hit, 2*self.y_hit, tile_size, "crouch_walk_r_2")

    def get_events(self, grid, lkeys):
        # get the pressed keys
        pressed_keys = pygame.key.get_pressed()

        o_x = self.x
        o_y = self.y

        self.isWalking = False
        self.onFloor = False

        if pressed_keys[pygame.K_SPACE] and not lkeys[pygame.K_SPACE] or pressed_keys[pygame.K_w] and not lkeys[pygame.K_w] or pressed_keys[pygame.K_UP] and not lkeys[pygame.K_UP]:
            if not self.singleJumped:
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
            self.velocity_up = self.gravity

        o_x = self.x
        o_y = self.y

        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if not self.isCrouching:
                self.hitbox = object.RectangularHitbox(1*self.x_hit, self.y_hit/2, 0.5, 0, -self.y_hit/2)
            self.isCrouching = True
        else:
            if self.isCrouching:
                self.hitbox = object.RectangularHitbox(self.x_hit, self.y_hit, 0.5)
                self.isCrouching = False
                if not self.is_valid(grid):
                    self.hitbox = object.RectangularHitbox(1*self.x_hit, self.y_hit / 2, 0.5, 0, -self.y_hit / 2)
                    self.isCrouching = True

        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.isCrouching:
                self.x -= self.crouchSpeed
            else:
                self.x -= self.speed
            self.direction = 1
            self.isWalking = True

        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
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
            self.velocity_up = self.gravity

    def dead(self):
        if self.y < 0:
            return True
        for g in gödi.gödi_list:
            if self.collide(g):
                return True
        for s in sand.sand_list:
            if self.collide(s):
                if not self.isCrouching:
                    if s.y > self.y + self.y_hit/2:
                        return True
                else:
                    if s.y > self.y - self.y_hit/4:
                        return True
        return False

    def draw(self, surface, camera, bigSprite, debug = False):
        # draw the player
        if self.isCrouching:
            if self.isWalking:
                if self.walkinframe == 1:
                    if self.direction == 1:
                        bigSprite["crouch_walk_l_1"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                    else:
                        bigSprite["crouch_walk_r_1"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                else:
                    if self.direction == 1:
                        bigSprite["crouch_walk_l_2"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                    else:
                        bigSprite["crouch_walk_r_2"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                if self.thisframe == 10:
                    self.walkinframe = 3 - self.walkinframe
                    self.thisframe = 0
                self.thisframe += 1
            else:
                if self.direction == 1:
                    bigSprite["crouch_l"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                else:
                    bigSprite["crouch_r"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))

        elif self.isWalking:
            if self.direction == 1:
                if self.walkinframe == 1:
                    bigSprite["walk_l_1"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                else:
                    bigSprite["walk_l_2"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
            else:
                if self.walkinframe == 1:
                    bigSprite["walk_r_1"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
                else:
                    bigSprite["walk_r_2"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
            if self.thisframe == 10:
                self.walkinframe = 3 - self.walkinframe
                self.thisframe = 0
            self.thisframe += 1

        elif not self.onFloor:
            if self.direction == 1:
                bigSprite["jump_l"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
            else:
                bigSprite["jump_r"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
        else:
            if self.direction == 0:
                bigSprite["player_r"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))
            else:
                bigSprite["player_l"].draw(surface, camera.coords_to_screen(self.x-self.x_hit * 2.5, self.y+self.y_hit, surface))

        if debug:
            for p in self.hitbox.points:
                pygame.draw.circle(surface, (255, 0, 0), camera.coords_to_screen(self.x + p[0],self.y + p[1], surface), 2)