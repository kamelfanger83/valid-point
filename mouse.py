import pygame
import gödi

def mouseclickleft(grid,camera,screen, x_y_prev):
    pos = pygame.mouse.get_pos()
    xy = camera.screen_to_coords(pos[0],pos[1], screen)
    x,y = int(xy[0]), int(xy[1])
    x_y_prev[0],x_y_prev[1] = int(x_y_prev[0]), int(x_y_prev[1])
    if [x,y] != x_y_prev:
        grid[x][y] = (grid[x][y]+1)%3
        return [x,y]
    else:
        return x_y_prev


def mouseclickmiddle(grid, ud_list):
    grid.load(".\maps\\test.gr")
    gödi.gödi_list = []
    ud_list.clear()

def mouseclickright(camera,screen,tile_size, ud_list):
    pos = pygame.mouse.get_pos()
    xy = camera.screen_to_coords(pos[0], pos[1], screen)
    x, y = xy[0], xy[1]

    gödi.Gödi(x, y, ".\\sprites\\gödi.png", tile_size, ud_list)





#if event.type == pygame.MOUSEBUTTONDOWN:
    # print(event.button)
# 1 - left click
# 2 - middle click
# 3 - right click
# 4 - scroll up
# 5 - scroll down