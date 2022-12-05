import pygame
import sprites
import object
import math

class Sand(object.Object):
    def __init__(self, x , y, sprite_path, tile_size, r = 0.75):
        self.x = x
        self.y = y
        self.sprite = sprites.Sprite(sprite_path, 2*r, 2*r, tile_size)

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

