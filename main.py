# PLATFORMER GAME

import pygame
import world
import player as player_module
import camera as camera_module
import sprites
import gödi
import mouse

# initialize a fullscreen pygame window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Platformer Game")

# Create grid

width = 100
height = 20

grid = world.Grid(width, height)

for column in range(width):
    grid[column][0] = 1

grid[0][1] = 1
grid[0][2] = 1

#grid[8][1] = 1
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
#grid[7][3] = 1


grid.store(".\maps\\test.gr")

tile_size = 100

camera = camera_module.Camera(tile_size)

# load grid images
ground = sprites.Sprite(".\sprites\\tile.jpg", 1, 1, tile_size)
bg = sprites.Sprite(".\sprites\\bg.jpg", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size)
death_pic = sprites.Sprite(".\sprites\\death_screen.png", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size)

player = player_module.Player(5, 2)
player.load_sprites(tile_size)


# create test gödi
gödi.Gödi(13, 1.5, ".\sprites\\gödi.png", tile_size)

def death_screen():
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    death_pic.draw(screen, (0, 0))

    pygame.display.update()
    pygame.time.Clock().tick(60)

def game_loop():
    while True:
     # EVENT HANDLING

    # pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ev_button = event.button
                if ev_button == 1:
                    mouse.mouseclickleft(grid, camera, screen)
                elif ev_button == 2:
                    mouse.mouseclickmiddle(grid)
                elif ev_button == 3:
                    mouse.mouseclickright(camera, screen, tile_size)

        # player controls
        player.get_events(grid)

        # UPDATE

        for g in gödi.gödi_list:
            g.step(grid)

            if g.y - g.y_hit < player.y + player.y_hit and g.y + g.y_hit > player.y - player.y_hit and g.x - g.x_hit < player.x + player.x_hit and g.x + g.x_hit > player.x - player.x_hit:
                death_screen()

        # DRAWING

        camera.xcen = player.x

        bg.draw(screen, (0, 0))

        # draw the grid
        for row in range(height):
            for column in range(width):
                if grid[column][row] == 1:
                    ground.draw(screen, camera.coords_to_screen(column, row+1, screen))

        # draw the player
        player.draw(screen, camera)

        # draw the gödis
        for g in gödi.gödi_list:
            g.draw(screen, camera)

        # update the screen
        pygame.display.update()
        pygame.time.Clock().tick(60)

game_loop()