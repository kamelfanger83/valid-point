import pygame
import sprites
import object
import math

respawnpoint_list = []


class Respawnpoint(object.Object):
    def __init__(self, x=None, y=None, tile_size=None, ud_list=None):
        if x == None:
            return
        self.x = x
        self.y = y

        self.ud_list = ud_list
        respawnpoint_list.append(self)
        ud_list.append(self)

        self.x_hit = 0.5
        self.y_hit = 0.5
        self.hitbox = object.RectangularHitbox(self.x_hit/2, self.y_hit/2, 0.2)


    def update(self, grid, ud_list):
        return

    def load(self, tile_size, bigSprite):
        bigSprite.load_sprite(".\\data\\img\\respawnpoint.jpg", 0.5, 0.5, tile_size, "respawnpoint")

    def draw(self, screen, camera, bigSprite):
        bigSprite["respawnpoint"].draw(screen, camera.coords_to_screen(self.x-self.x_hit/2, self.y+self.y_hit/2, screen))