import pygame
import sprites

button_list = []
all_buttons = []
dim = ["square", "rectangle"]
dimensions = [[1, 1],[2, 0.5]]

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
    bigSprite.load_sprite(".\\sprites\\item_bg.jpg", 1, 1, tile_size, "square")
    bigSprite.load_sprite(".\\sprites\\item_bg.jpg", 2, 0.5, tile_size, "rectangle")
