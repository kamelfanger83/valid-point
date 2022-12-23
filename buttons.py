import pygame
import sprites

# main_menu, creative, survival

button_list = []

class Button:
    def __init__(self, x=None, y=None, w=None, h=None, path=None, action =None, center=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.path = path
        self.center = center

        self.action = action

        if not self.x is None:
            button_list.append(self)

    def on(self, pos):
        if self.x - self.w / 2 < pos[0] < self.x + self.w / 2 and self.y - self.h / 2 < pos[1] < self.y + self.h / 2:
            return True
        return False

    def click(self):
        self.action()

    def load(self, tile_size, bigSprite):
        bigSprite.load_sprite(self.path, self.w/tile_size, self.h/tile_size, tile_size)

    def draw(self, tile_size, screen, bigSprite):
        lt = (self.x, self.y)
        if self.center:
            lt = (self.x - self.w / 2, self.y - self.h / 2)
        bigSprite.get_by_tuple(self.path, self.w/tile_size, self.h/tile_size).draw(screen, lt)
