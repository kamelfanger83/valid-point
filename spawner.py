import gödi
import sprites

spawner_list = []
class Spawner:
    def __init__(self, x, y, interval, tile_size, grid, ud_list):
        self.x = x
        self.y = y
        self.interval = interval
        self.spawn_interval = 30
        self.tile_size = tile_size

        grid[x][y] = 3
        grid[x][y+1] = 3
        grid[x+1][y] = 3
        grid[x+1][y+1] = 3

        self.ticks = 0

        self.sprite_idle = sprites.Sprite(".\\sprites\\spawner_idle.png", 2, 2, tile_size)
        self.sprite_spawn = sprites.Sprite(".\\sprites\\spawner_spawn.png", 2, 2, tile_size)
        self.spawning = False

        spawner_list.append(self)
        ud_list.append(self)
        self.ud_list = ud_list

    def draw(self, surface, camera):
        if self.spawning:
            self.sprite_spawn.draw(surface, camera.coords_to_screen(self.x, self.y + 2, surface))
        else:
            self.sprite_idle.draw(surface, camera.coords_to_screen(self.x, self.y + 2, surface))

    def update(self, grid, ud_list):
        self.ticks += 1
        if self.ticks == self.interval:
            self.spawning = True
            gödi.Gödi(self.x, self.y, ".\\sprites\\gödi.png", self.tile_size, self.ud_list)
        if self.ticks == self.interval + self.spawn_interval:
            self.ticks = 0
            self.spawning = False
