import pygame
import sprites

gödi_list = []

class Gödi:
    def __init__(self, x , y, sprite_path, tile_size, r = 0.499):
        self.x = x
        self.y = y
        self.sprite = sprites.Sprite(sprite_path, 2*r, 2*r, tile_size)
        self.x_hit = r
        self.y_hit = r

        self.vert = 1 # 0 = right, 1 = left
        self.speed = 0.1
        self.ang = 0
        self.ang_speed = 10

        self.climbing = False
        self.up_speed = 0
        self.gravity = 0.02

        gödi_list.append(self)

    def is_valid(self, grid):
        if grid[int(self.x - self.x_hit)][int(self.y - self.y_hit)] == 0 and \
           grid[int(self.x + self.x_hit)][int(self.y - self.y_hit)] == 0 and \
           grid[int(self.x - self.x_hit)][int(self.y + self.y_hit)] == 0 and \
           grid[int(self.x + self.x_hit)][int(self.y + self.y_hit)] == 0:
            return True
        return False


    def step(self, grid):
        self.climbing = False

        if self.vert == 1:
            if(self.x - self.speed < 0):
                gödi_list.remove(self)
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

    def draw(self, surface, camera):
        #   rotate gödi image by self.ang then draw that image
        #   rotate around the center of the image

        #   get the rotated image
        rotated_image = pygame.transform.rotate(self.sprite.image, self.ang)

        #   get the rectangle of the rotated image
        rect = rotated_image.get_rect()

        #   set the center of the rectangle to the center of the image
        rect.center = camera.coords_to_screen(self.x, self.y, surface)

        #   draw the rotated image
        surface.blit(rotated_image, rect)