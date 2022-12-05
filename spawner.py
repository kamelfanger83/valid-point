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

        self.ospawning = None

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
            self.ospawning = gödi.Gödi(self.x+0.1, self.y+0.5, ".\\sprites\\gödi.png", self.tile_size, self.ud_list, 0.05)
            self.ospawning.speed = 0
            self.ospawning.ang_speed = 0
            self.ospawning.gravity = 0

        if self.interval < self.ticks < self.interval + self.spawn_interval:
            x = (self.ticks-self.interval) / self.spawn_interval
            self.ospawning.x = self.x + (1-x)*0.1 + x * -0.9
            self.ospawning.r = (1-x) * 0.05 + x * 0.75
            self.ospawning.update_r()

        if self.ticks == self.interval + self.spawn_interval:
            self.ticks = 0
            self.spawning = False
            self.ospawning.speed = 0.1
            self.ospawning.gravity = 0.02
            self.ospawning.vert = 1
            self.ospawning.update_r()