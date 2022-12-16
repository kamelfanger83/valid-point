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
creative_player = None

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
    ud_list = []

    width = 100
    height = 20

    grid = world.Grid(width, height)

    for column in range(width):
        grid[column][0] = 1

    grid[0][1] = 1
    grid[0][2] = 1

    # grid[8][1] = 1
    grid[8][2] = 1
    grid[8][3] = 1
    grid[8][4] = 1
    grid[8][5] = 1

    grid[10][1] = 1
    grid[10][2] = 1
    grid[10][3] = 1
    grid[10][4] = 1
    grid[10][5] = 1
    grid[10][6] = 1
    grid[10][7] = 1

    grid[9][8] = 1

    grid[1][3] = 1
    # grid[7][3] = 1

    player = player_module.Player(5, 2)

    # create test spawner
    spawner.Spawner(13, 5, 120, tile_size, grid, ud_list)


def game_loop():
    x_y_previous = [-1,-1]
    while True:
     # EVENT HANDLING

    # pygame events
        for event in pygame.event.get():
            mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons = 3)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif mouse_buttons_pressed[0] == True:
                x_y_previous = mouse.mouseclickleft(grid, camera, screen, x_y_previous)
            elif event.type == pygame.MOUSEBUTTONUP:
                ev_button = event.button
                if ev_button == 1:
                    x_y_previous = [-1,-1]
                elif ev_button == 2:
                    mouse.mouseclickmiddle(grid, ud_list)
                elif ev_button == 3:
                    mouse.mouseclickright(camera, screen, tile_size, ud_list)

      # player controls
        player.get_events(grid)

        # UPDATE

        for thing in ud_list:
            thing.update(grid, ud_list)

        if player.dead():
            death_screen()
            return

        # DRAWING

        camera.xcen = player.x

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