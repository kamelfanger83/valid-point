import pygame
import sprites
import object
import math

sand_list = []


class Sand(object.Object):
    def __init__(self, x=None, y=None, tile_size=None, ud_list=None):
        if x == None:
            return
        self.x = x
        self.y = y

        self.ud_list = ud_list
        sand_list.append(self)
        ud_list.append(self)

        self.x_hit = 1
        self.y_hit = 1
        self.hitbox = object.RectangularHitbox(0.5, 0.5, 0.2)

        self.speed = 0.05
        self.gravity = 0.02

    def update(self, grid, ud_list):
        if grid[self.x][int(self.y - self.speed)] != 0:
            grid[self.x][int(self.y - self.speed) + 1] = 2
            sand_list.remove(self)
            ud_list.remove(self)
        else:
            self.y = self.y - self.speed
            self.speed += self.gravity
            
    def load(self, tile_size, bigSprite):
        bigSprite.load_sprite("./data/img/sand.jpg", 1, 1, tile_size, "sand")

    def draw(self, screen, camera, bigSprite):
        bigSprite["sand"].draw(screen, camera.coords_to_screen(self.x, self.y + 1, screen))


def is_valid(x, y, grid, tile_size, ud_list):
    if grid[x][y-1] != 0:
        return True
    else:
        Sand(x, y, tile_size, ud_list)
        grid[x][y] = 0
        return False