# PLATFORMER GAME

import pygame
import world
import player as player_module
import camera as camera_module
import sprites
import gödi
import mouse
import time
import spawner
import sand

# initialize a fullscreen pygame window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Platformer Game")

tile_size = 100

camera = camera_module.Camera(tile_size)

bigSprite = sprites.Sprites()

# load grid images
bigSprite.load_sprite(".\\sprites\\tile.jpg", 1, 1, tile_size, "tile")
bigSprite.load_sprite(".\\sprites\\sand.jpg", 1, 1, tile_size, "sand")
bigSprite.load_sprite(".\\sprites\\bg.jpg", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "bg")
bigSprite.load_sprite(".\\sprites\\death_screen.png", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "death_screen")
bigSprite.load_sprite(".\\sprites\\menu.png", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "menu")

grid = None
player = None
creative = False

creative_speed = 0.1

ud_list = []

def load():
    player_module.Player().load(tile_size, bigSprite)
    gödi.Gödi().load(tile_size, bigSprite)
    spawner.Spawner().load(tile_size, bigSprite)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_game()
                    game_loop()

        bigSprite["menu"].draw(screen, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)


def death_screen():
    start = time.time()
    
    while time.time() - start < 3:
        # pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        bigSprite["death_screen"].draw(screen, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)

def init_game():
    global grid
    global player
    global ud_list

    gödi.gödi_list = []
    sand.sand_list = []
    ud_list = []

    width = 100
    height = 20

    grid = world.Grid(width, height)

    grid.load(".\\maps\\test.gr")

    player = player_module.Player(5, 2)

    # load spawner
    for x in range(height):
        for y in range(width):
            try:
                if grid[x][y] == 3:
                    spawner.Spawner(x, y, 120, tile_size, grid, ud_list)
            except:
                pass

def game_loop():
    global creative

    p_previous = False
    x_y_previous = [-1,-1]
    while True:
        # No mouse in survival
        if creative:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

        np_previous = False
        # EVENT HANDLING

        # pygame events
        for event in pygame.event.get():
            mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons = 3)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif mouse_buttons_pressed[0] == True and creative:
                x_y_previous = mouse.mouseclickleft(grid, camera, screen, x_y_previous)
            elif event.type == pygame.MOUSEBUTTONUP and creative:
                ev_button = event.button
                if ev_button == 1:
                    x_y_previous = [-1,-1]
                elif ev_button == 2:
                    mouse.mouseclickmiddle(grid, ud_list)
                elif ev_button == 3:
                    mouse.mouseclickright(camera, screen, tile_size, ud_list)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            if p_previous == False:
                creative = not creative
            np_previous = True
        p_previous = np_previous

        # player controls
        if creative:
            # get keys and move camera xcen and ycen with wasd
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                camera.ycen += creative_speed
            if keys[pygame.K_s]:
                camera.ycen -= creative_speed
            if keys[pygame.K_a]:
                camera.xcen -= creative_speed
            if keys[pygame.K_d]:
                camera.xcen += creative_speed

        else:
            player.get_events(grid)
            camera.xcen = player.x
            camera.ycen = player.y - 1.8

        # UPDATE

        for thing in ud_list:
            thing.update(grid, ud_list)

        if player.dead() and not creative:
            death_screen()
            return

        # DRAWING

        bigSprite["bg"].draw(screen, (0, 0))

        # draw the grid
        for row in range(len(grid[0])):
            for column in range(len(grid)):
                if grid[column][row] == 1:
                    bigSprite["tile"].draw(screen, camera.coords_to_screen(column, row+1, screen))
                if grid[column][row] == 2 and sand.is_valid(column,row, grid, tile_size, ud_list) == True:
                    bigSprite["sand"].draw(screen, camera.coords_to_screen(column, row+1, screen))
                if grid[column][row] == 3:
                    pass


        # draw the player
        player.draw(screen, camera, bigSprite)

        # draw the things in ud_list
        for thing in ud_list:
            thing.draw(screen, camera, bigSprite)

        # update the screen
        pygame.display.update()
        pygame.time.Clock().tick(60)

load()
main_menu()
