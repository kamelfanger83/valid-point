import pygame
import gödi

def mouseclickleft(grid,camera,screen):
    pos = pygame.mouse.get_pos()
    xy = camera.screen_to_coords(pos[0],pos[1], screen)
    x,y = int(xy[0]), int(xy[1])
    print(x,y)
    grid[x][y] = (grid[x][y]+1)%2

def mouseclickmiddle(grid):
    grid.load(".\maps\\test.gr")
    gödi.gödi_list = []

def mouseclickright(camera,screen,tile_size):
    pos = pygame.mouse.get_pos()
    xy = camera.screen_to_coords(pos[0], pos[1], screen)
    x, y = int(xy[0]), int(xy[1])

    gödi.Gödi(x, y, ".\sprites\\gödi.png", tile_size)





#if event.type == pygame.MOUSEBUTTONDOWN:
    # print(event.button)
# 1 - left click
# 2 - middle click
# 3 - right click
# 4 - scroll up
# 5 - scroll down