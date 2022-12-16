import pygame
import sprites

#main_menu, creative, survival

button_list = []
all_buttons = []
dim = ["square", "rectangle"]
dimensions = [[1, 1],[3, 0.75]]

class Button:
    def __init__(self, x, y, form, menu):
        self.x = x
        self.y = y
        self.menu = menu
        self.form = dimensions[form]
        self.sprite = dim[form]
        all_buttons.append(self)
    def draw(self, screen, bigSprite, tile_size):
        bigSprite[self.sprite].draw(screen, (tile_size*self.x, screen.get_height()-tile_size*self.y))


def loadsprites(tile_size, bigSprite):
    bigSprite.load_sprite(".\\sprites\\item_bg.jpg", dimensions[0][0], dimensions[0][1], tile_size, dim[0])
    bigSprite.load_sprite(".\\sprites\\item_bg.jpg", dimensions[1][0], dimensions[1][1], tile_size, dim[1])
