import pygame
import sprites
import object
import math

gödi_list = []

class Gödi(object.Object):
    def __init__(self, x = 0, y = 0, filePath = "", ud_list = [], r = 0.75):
        self.x = x
        self.y = y
        self.path = filePath

        self.x_hit = r
        self.y_hit = r
        self.hitbox = object.RectangularHitbox(r, r, 0.5)

        self.vert = 1 # 0 = right, 1 = left
        self.speed = 0.1
        self.ang = 0
        self.ang_speed = 360 / (r*2*math.pi) * self.speed

        self.climbing = False
        self.up_speed = 0
        self.gravity = 0.02

        gödi_list.append(self)
        ud_list.append(self)

    def load(self, tile_size, bigSprite):
        bigSprite.load_sprite("./data/img/gödi.png", 2*self.x_hit, 2*self.y_hit, tile_size, "gödi")

    def update_r(self):
        self.x_hit = self.r
        self.y_hit = self.r
        self.hitbox = object.RectangularHitbox(self.r, self.r, 0.5)

        self.ang_speed = 360 / (self.r * 2 * math.pi) * self.speed

    def update(self, grid, ud_list):
        self.climbing = False

        if self.vert == 1:
            if(self.x - self.speed < 0):
                gödi_list.remove(self)
                ud_list.remove(self)
            self.ang += self.ang_speed

            self.x -= self.speed

            if not self.is_valid(grid):
                self.x += self.speed
                self.y += self.speed
                if not self.is_valid(grid):
                    self.y -= self.speed
                    self.vert = 0
                else:
                    self.climbing = True

            self.up_speed -= self.gravity
            self.y += self.up_speed

            if not self.is_valid(grid) or self.climbing:
                self.y -= self.up_speed
                self.up_speed = 0

        else:
            if(self.x + self.speed > grid.width-1):
                gödi_list.remove(self)
                ud_list.remove(self)
            self.ang -= self.ang_speed

            self.x += self.speed

            if not self.is_valid(grid):
                self.x -= self.speed
                self.y += self.speed
                if not self.is_valid(grid):
                    self.y -= self.speed
                    self.vert = 1
                else:
                    self.climbing = True

            self.up_speed -= self.gravity
            self.y += self.up_speed

            if not self.is_valid(grid) or self.climbing:
                self.y -= self.up_speed
                self.up_speed = 0

    def draw(self, surface, camera, bigSprite):
        #   rotate gödi image by self.ang then draw that image
        #   rotate around the center of the image

        #   get the rotated image
        rotated_image = pygame.transform.rotate(bigSprite.get_by_tuple(self.path, 2*self.x_hit, 2*self.y_hit).image, self.ang)

        #   get the rectangle of the rotated image
        rect = rotated_image.get_rect()

        #   set the center of the rectangle to the center of the image
        rect.center = camera.coords_to_screen(self.x, self.y, surface)

        #   draw the rotated image
        surface.blit(rotated_image, rect)