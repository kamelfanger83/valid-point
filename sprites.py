import pygame

sprite_list = []

class Sprite:
    def __init__(self, path, width, height, tile_size):
        self.image = pygame.image.load(path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * tile_size), int(height * tile_size)))
        sprite_list.append(self)

    def draw(self, surface, location):
        surface.blit(self.image, location)

class Sprites:
    def __init__(self):
        self.loaded_name = {}
        self.loaded_tuple = {}

    def load_sprite(self, path, size_x, size_y, tile_size, name = ""):
        if (path, size_x, size_y) in self.loaded_tuple:
            if name != "":
                self.loaded_name[name] = self.loaded_tuple[(path, size_x, size_y)]
        sprite = Sprite(path, size_x, size_y, tile_size)
        self.loaded_tuple[(path, size_x, size_y)] = sprite
        if name != "":
            self.loaded_name[name] = sprite

    def __getitem__(self, name):
        return self.loaded_name[name]

    def get_by_tuple(self, path, size_x, size_y):
        return self.loaded_tuple[(path, size_x, size_y)]