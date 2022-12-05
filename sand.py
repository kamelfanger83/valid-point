import pygame
import sprites
import object
import math

sand_list = []

class Sand(object.Object):
    def __init__(self, x , y, sprite_path, tile_size, ud_list):
        self.x = x
        self.y = y
        self.sprite = sprites.Sprite(sprite_path, 1, 1, tile_size)

        self.ud_list = ud_list
        sand_list.append(self)
        ud_list.append(self)

        self.x_hit = 1
        self.y_hit = 1
        self.hitbox = object.RectangularHitbox(1, 1, 0.5)

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

    def draw(self, screen, camera):
        self.sprite.draw(screen, camera.coords_to_screen(self.x, self.y + 1, screen))


def is_valid(x, y, grid, tile_size, ud_list):
    if grid[x][y-1] != 0:
        return True
    else:
        Sand(x, y, ".\sprites\\sand.jpg", tile_size, ud_list)
        grid[x][y] = 0
        return False


