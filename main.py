# PLATFORMER GAME
# implemented using pygame

import pygame
import world
import player as player_module
import camera as camera_module
import sprites
import gödi

# initialize pygame
pygame.init()

# create a fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# set the window title
pygame.display.set_caption("Platformer Game")

# drid is stored in a 2D list
width = 100
height = 20

# LOWEST ROW IS THE GROUND
# Positive x is right, positive y is up

# the first dimension of the grid represents the x cordinate and thus the left and right on the screen
# the second dimension of the grid represents the y cordinate and thus the up and down on the screen

grid = world.Grid(width, height)

for column in range(width):
    grid[column][0] = 1

grid[0][1] = 1
grid[0][2] = 1

#grid[8][1] = 1
grid[8][2] = 1

grid[1][3] = 1
#grid[7][3] = 1

tile_size = 100

camera = camera_module.Camera(tile_size)

# load grid images
ground = sprites.Sprite(".\sprites\\tile.jpg", 1, 1, tile_size)
bg = sprites.Sprite(".\sprites\\bg.jpg", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size)

player = player_module.Player(5, 2)
player.load_sprites(tile_size)

# load gödi image
gödi_sprite = sprites.Sprite(".\sprites\\gödi.png", 1, 1, tile_size)

gödi.Gödi()

gödiTicks = 0

while True:
    #event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            pygame.quit()
            exit(0)

    player.get_events(grid)

    if gödiTicks == 1:
        gödiTicks = 0
        for g in gödi.gödi_list:
            g.step(grid)
    gödiTicks += 1

    # draw the background such that height of the image is the height of the screen, repeat the image so whole grid gets covered
    bg.draw(screen, (0, 0))

    # draw the grid
    for row in range(height):
        for column in range(width):
            if grid[column][row] == 1:
                # place tiles so that the bottom left corner of the image is at the bottom left corner of the cell
                # lower left corner of the screen is (0, 0)
                # the first dimension of the grid represents the x cordinate and thus the left and right on the screen
                # the second dimension of the grid represents the y cordinate and thus the up and down on the screen
                ground.draw(screen, camera.coords_to_screen(column, row+1, screen))

    camera.xcen = player.x

    player.draw(screen, camera)

    # draw the gödil
    for g in gödi.gödi_list:
        g.draw(screen, camera, gödi_sprite)

    # update the screen
    pygame.display.update()

    # set the frame rate
    pygame.time.Clock().tick(60)