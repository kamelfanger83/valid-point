import pygame

sprite_list = []

class Sprite:
    def __init__(self, path, width, height, tile_size):
        self.image = pygame.image.load(path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (width * tile_size, height * tile_size))
        sprite_list.append(self)

    def draw(self, surface, location):
        surface.blit(self.image, location)