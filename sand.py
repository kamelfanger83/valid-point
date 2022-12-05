import pygame
import sprites
import object
import math

sand_list = []

class Sand(object.Object):
    def __init__(self, x , y, sprite_path, tile_size, r = 0.75):
        self.x = x
        self.y = y
        self.sprite = sprites.Sprite(sprite_path, 2*r, 2*r, tile_size)

        self.x_hit = r
        self.y_hit = r
        self.hitbox = object.RectangularHitbox(r, r, 0.5)

        self.speed = 0.05
        self.gravity = 0.02

    def fall(self, grid):
        if grid[self.x][int(self.y - self.speed)] != 0:
            grid[self.x][int(self.y - self.speed) + 1] = 2
            sand_list.remove(self)
            return True
        else:
            self.y = self.y - self.speed
            self.speed += self.gravity
            return False


def is_valid(x, y, grid, tile_size):
    if grid[x][y-1] != 0:
        return True
    else:
        sand_check = Sand(x, y, ".\sprites\\sand.jpg", tile_size, 2)
        sand_list.append(sand_check)
        grid[x][y] = 0
        return False


