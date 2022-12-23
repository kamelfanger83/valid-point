import pygame
import world
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

def init(bigSprite, screen, tile_size, activewindow, map):
    global grid
    global player
    global ud_list
    global debug
    global respawn
    global lkeys
    global x_y_previous
    global camera

    gödi.gödi_list = []
    sand.sand_list = []
    ud_list = []
    buttons.button_list = []

    width = 100
    height = 20

    grid = world.Grid(width, height)

    grid.load(".\\maps\\"+map+".gr", tile_size, ud_list)

    player = player_module.Player(5, 2)

    debug = False
    respawn = False

    lkeys = pygame.key.get_pressed()

    x_y_previous = [-1, -1]

    camera = camera_module.Camera(tile_size)

    return "show_game"
def run(bigSprite, screen, tile_size, activewindow):
    global creative
    global player
    global debug
    global respawn
    global lkeys
    global x_y_previous
    global camera

    for event in pygame.event.get():
        mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons=3)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif mouse_buttons_pressed[0] == True and creative:
            x_y_previous = mouse.mouseclickleft(grid, camera, screen, x_y_previous)
        elif event.type == pygame.MOUSEBUTTONUP and creative:
            ev_button = event.button
            if ev_button == 1:
                x_y_previous = [-1, -1]
            elif ev_button == 2:
                mouse.mouseclickmiddle(grid, tile_size, ud_list)
            elif ev_button == 3:
                mouse.mouseclickright(camera, screen, tile_size, ud_list)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_p] and not lkeys[pygame.K_p]:
        creative = not creative
        if creative:
            for i in range(len(buttons.all_buttons)):
                if buttons.all_buttons[i].menu == "creative":
                    buttons.button_list.append(buttons.all_buttons[i])
        else:
            buttons.all_buttons = []

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
                mouse.mouseclickmiddle(grid, tile_size, ud_list)
                player = player_module.Player(5, 2)
            else:
                return "show_death"

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

    # draw the player
    player.draw(screen, camera, bigSprite, debug)

    # draw the things in ud_list
    for thing in ud_list:
        thing.draw(screen, camera, bigSprite)

    # draw buttons
    for i in range(len(buttons.button_list)):
        buttons.button_list[i].draw(screen, bigSprite, tile_size)

    # update the screen
    pygame.display.update()
    pygame.time.Clock().tick(60)

    return activewindow
