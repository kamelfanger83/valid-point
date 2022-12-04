class Camera:
    def __init__(self, tileSize, xcen = 0):
        self.tileSize = tileSize
        self.xcen = xcen

    def coords_to_screen(self, x, y, surface):
        return ((x - self.xcen) * self.tileSize + surface.get_width()/2, surface.get_height() - (y * self.tileSize))

    def screen_to_coords(self, x, y, surface):
        return ((x - surface.get_width() / 2) / self.tileSize + self.xcen, (surface.get_height() - y) / self.tileSize)