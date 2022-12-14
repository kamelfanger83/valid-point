import pygame
import gödi
import buttons

x_y_prev = [-1, -1]

def mouseclickleft(grid, camera, screen, activeWindow):
    global x_y_prev
    pos = pygame.mouse.get_pos()
    for button in buttons.button_list:
        if button.on(pos):
            button.click()
    if activeWindow == "game":
        xy = camera.screen_to_coords(pos[0], pos[1], screen)
        x, y = int(xy[0]), int(xy[1])
        x_y_prev[0], x_y_prev[1] = int(x_y_prev[0]), int(x_y_prev[1])
        if [x, y] != x_y_prev:
            if 0 <= x < grid.width and 0 <= y < grid.height:
                grid[x][y] = (grid[x][y] + 1) % 3
            x_y_prev = [x, y]


def mouseclickmiddle(grid, tile_size, ud_list):
    gödi.gödi_list = []
    ud_list.clear()
    grid.load(".\maps\\jumpandgian.gr", tile_size, ud_list)


def mouseclickright(camera, screen, tile_size, ud_list):
    pos = pygame.mouse.get_pos()
    xy = camera.screen_to_coords(pos[0], pos[1], screen)
    x, y = xy[0], xy[1]

    gödi.Gödi(x, y, ".\\data\\img\\gödi.png", ud_list)

# if event.type == pygame.MOUSEBUTTONDOWN:
# print(event.button)
# 1 - left click
# 2 - middle click
# 3 - right click
# 4 - scroll up
# 5 - scroll down
