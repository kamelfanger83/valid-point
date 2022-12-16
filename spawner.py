import gödi
import sprites

spawner_list = []
class Spawner:
    def __init__(self, x=None, y=None, interval=None, tile_size=None, grid=None, ud_list=None):
        self.spawn_interval = 30
        if x == None:
            return

        self.x = x
        self.y = y
        self.interval = interval
        self.tile_size = tile_size

        grid[x][y] = 3
        grid[x][y+1] = 3
        grid[x+1][y] = 3
        grid[x+1][y+1] = 3

        self.ticks = 0
        self.spawning = False

        self.ospawning = None

        spawner_list.append(self)
        ud_list.append(self)
        self.ud_list = ud_list

    def load(self, tile_size, bigSprite):
        bigSprite.load_sprite(".\\sprites\\spawner_idle.png", 2, 2, tile_size, "spawner_idle")
        bigSprite.load_sprite(".\\sprites\\spawner_spawn.png", 2, 2, tile_size, "spawner_spawn")

        for spawning_frame in range(self.spawn_interval):
            x = spawning_frame / self.spawn_interval
            r = (1-x) * 0.05 + x * 0.75
            bigSprite.load_sprite(".\\sprites\\gödi.png", 2*r, 2*r, tile_size)

    def draw(self, surface, camera, bigSprite):
        if self.spawning:
            bigSprite["spawner_spawn"].draw(surface, camera.coords_to_screen(self.x, self.y + 2, surface))
        else:
            bigSprite["spawner_idle"].draw(surface, camera.coords_to_screen(self.x, self.y + 2, surface))

    def update(self, grid, ud_list):
        self.ticks += 1
        if self.ticks == self.interval:
            self.spawning = True
            self.ospawning = gödi.Gödi(self.x+0.1, self.y+0.5, ".\\sprites\\gödi.png", self.ud_list, 0.05)
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