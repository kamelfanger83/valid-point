import pygame
import utils.world
import player as player_module
import camera as camera_module
import sprites
import gödi
import mouse
import time
import spawner
import buttons
import sand

grid = None
player = None
creative = False
debug = False
respawn = False
lkeys = None
x_y_previous = []

creative_speed = 0.1

ud_list = []

camera = None
map = None

def init(bigSprite, screen, tile_size, activewindow, maparg):
    global grid
    global player
    global ud_list
    global debug
    global respawn
    global lkeys
    global x_y_previous
    global camera
    global map
    map = maparg

    camera = camera_module.Camera(tile_size)

    gödi.gödi_list = []
    sand.sand_list = []
    ud_list = []

    width = 100
    height = 20

    grid = utils.world.Grid(width, height)

    grid.load(".\\data\\maps\\"+map+".gr", tile_size, ud_list)

    player = player_module.Player(5, 2)

    debug = False
    respawn = False

    lkeys = pygame.key.get_pressed()

    x_y_previous = [-1, -1]

def show(bigSprite, screen, tile_size, activewindow):
    global creative
    global player
    global debug
    global respawn
    global lkeys
    global x_y_previous
    global camera
    
    while True:
        for event in pygame.event.get():
            mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons=3)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif mouse_buttons_pressed[0] == True and creative:
                mouse.mouseclickleft(grid, camera, screen, "game")
            elif event.type == pygame.MOUSEBUTTONUP and creative:
                ev_button = event.button
                if ev_button == 1:
                    mouse.x_y_prev = [-1, -1]
                elif ev_button == 2:
                    mouse.mouseclickmiddle(grid, tile_size, ud_list, "game", map)
                elif ev_button == 3:
                    mouse.mouseclickright(camera, screen, tile_size, ud_list, "game")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and not lkeys[pygame.K_p]:
            creative = not creative
            if creative:
                pass
                # append creative buttons
            else:
                pass
                # remove creative buttons

        if keys[pygame.K_b] and not lkeys[pygame.K_b] and creative:
            debug = not debug
        if keys[pygame.K_r] and not lkeys[pygame.K_r] and creative:
            respawn = not respawn
        if keys[pygame.K_q] and not lkeys[pygame.K_q] and creative:
            output = ""

            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] != 0:
                        output += str(x) + " " + str(y) + " " + str(grid[x][y]) + "\n"

            print(output)

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
            player.get_events(grid, lkeys)
            camera.xcen = player.x
            camera.ycen = player.y - 1.8

        # UPDATE

        if not creative:
            for thing in ud_list:
                thing.update(grid, ud_list)
            if player.dead():
                if respawn:
                    player = player_module.Player(player.rx, player.ry)
                else:
                    return "death"

        lkeys = keys

        # DRAWING

        bigSprite["bg"].draw(screen, (0, 0))

        # draw the grid
        for row in range(len(grid[0])):
            for column in range(len(grid)):
                if not creative and grid[column][row] == 2:
                    sand.is_valid(column, row, grid, tile_size, ud_list)
                if grid[column][row] == 1:
                    bigSprite["tile"].draw(screen, camera.coords_to_screen(column, row + 1, screen))
                if grid[column][row] == 2:
                    bigSprite["sand"].draw(screen, camera.coords_to_screen(column, row + 1, screen))
                if grid[column][row] == 3:
                    pass

        if debug:
            # draw grid lines using pygame line function
            for row in range(len(grid[0])):
                pygame.draw.line(screen, (255, 255, 255), camera.coords_to_screen(0, row, screen), camera.coords_to_screen(len(grid), row, screen))
            for column in range(len(grid)):
                pygame.draw.line(screen, (255, 255, 255), camera.coords_to_screen(column, 0, screen), camera.coords_to_screen(column, len(grid[0]), screen))


        # draw the things in ud_list
        for thing in ud_list:
            thing.draw(screen, camera, bigSprite)

        # draw the player
        player.draw(screen, camera, bigSprite, debug)

        # update the screen
        pygame.display.update()
        pygame.time.Clock().tick(60)