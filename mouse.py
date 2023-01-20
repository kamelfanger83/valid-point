import pygame
import gödi
import respawnpoint
import spawner
import winblock
import buttons

x_y_prev = [-1, -1]


def mouseclickleft(grid, camera, screen, menu, args=None):
    global x_y_prev
    pos = pygame.mouse.get_pos()
    for button in buttons.button_list:
        if button.on(pos):
            button.click()
    if menu == "game":
        xy = camera.screen_to_coords(pos[0], pos[1], screen)
        x, y = int(xy[0]), int(xy[1])
        x_y_prev[0], x_y_prev[1] = int(x_y_prev[0]), int(x_y_prev[1])
        if [x, y] != x_y_prev:
            if 0 <= x < grid.width and 0 <= y < grid.height:
                grid[x][y] = args
            x_y_prev = [x, y]


def mouseclickmiddle(grid, tile_size, ud_list, menu, map, args=None):
    if menu == "game":
        gödi.gödi_list = []
        ud_list.clear()
        grid.load(".\\data\\maps\\" + map + ".gr", tile_size, ud_list)


def mouseclickright(camera, screen, tile_size, ud_list, menu, grid, args=None):
    if menu == "game":
        pos = pygame.mouse.get_pos()
        xy = camera.screen_to_coords(pos[0], pos[1], screen)
        x, y = xy[0], xy[1]

        if args == 3:
            spawner.Spawner(int(x), int(y), 100, tile_size, grid, ud_list)
        elif args == 4:
            gödi.Gödi(x, y, ".\\data\\img\\gödi.png", ud_list)
        elif args == 5:
            respawnpoint.Respawnpoint(int(x) + 0.5, int(y) + 0.5, ".\\data\\img\\respawnpoint.jpg", ud_list)
        elif args == 6:
            winblock.Winblock(int(x) + 0.5, int(y) + 0.5, ".\\data\\img\\respawnpoint.jpg", ud_list)

# if event.type == pygame.MOUSEBUTTONDOWN:
# print(event.button)
# 1 - left click
# 2 - middle click
# 3 - right click
# 4 - scroll up
# 5 - scroll down
