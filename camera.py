class Camera:
    def __init__(self, tileSize, xcen = 0, ycen = 0):
        self.tileSize = tileSize
        self.xcen = xcen
        self.ycen = ycen


    def coords_to_screen(self, x, y, surface):
        return ((x - self.xcen) * self.tileSize + surface.get_width()/2, surface.get_height() - ((y - self.ycen) * self.tileSize) - surface.get_height()/2)

    def screen_to_coords(self, x, y, surface):
        return ((x - surface.get_width()/2)/self.tileSize + self.xcen, (surface.get_height() - y - surface.get_height()/2)/self.tileSize + self.ycen)
        #return ((x - surface.get_width() / 2) / self.tileSize + self.xcen, (surface.get_height() - y + surface.get_height()/2) / self.tileSize + self.ycen)