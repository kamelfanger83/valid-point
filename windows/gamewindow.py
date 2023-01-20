import random

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
import winblock
import respawnpoint

grid = None
player = None
creative = False
debug = False
respawn = False
lkeys = None
x_y_previous = []
allBlocks = [[0, "select_nothing"], [1, "tile"], [2, "sand"], [7, "death_block"]]
allObjects = [[0, "select_nothing"], [3, "select_spawner"], [4, "select_gödi"], [5, "select_respawnpoint"], [6, "select_winblock"]]

selectedObject = 4
selectedBlock = 1

creative_speed = 0.1

ud_list = []

camera = None
map = None

kActive = False
lActive = False

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
    global window
    map = maparg

    camera = camera_module.Camera(tile_size)

    window = utils.windowbuilder.WindowBuilder(screen)

    gödi.gödi_list = []
    sand.sand_list = []
    spawner.spawner_list = []
    winblock.winblock_list = []
    respawnpoint.respawnpoint_list = []
    ud_list = []

    width = 100
    height = 20

    grid = utils.world.Grid(width, height)

    grid.load(".\\data\\maps\\"+map+".gr", tile_size, ud_list)

    player = player_module.Player(9, 2)

    debug = False
    respawn = False

    lkeys = pygame.key.get_pressed()

    x_y_previous = [-1, -1]

    kActive = False
    lActive = False

def show(bigSprite, screen, tile_size, activewindow):
    global creative
    global player
    global debug
    global respawn
    global lkeys
    global x_y_previous
    global camera
    global selectedBlock
    global selectedObject
    global kActive
    global lActive
    
    while True:
        for event in pygame.event.get():
            mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons=3)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif mouse_buttons_pressed[0] == True and creative and not kActive and not lActive:
                mouse.mouseclickleft(grid, camera, screen, "game", selectedBlock)
            elif event.type == pygame.MOUSEBUTTONUP and creative and not lActive and not kActive:
                ev_button = event.button
                if ev_button == 1:
                    mouse.x_y_prev = [-1, -1]
                elif ev_button == 2:
                    mouse.mouseclickmiddle(grid, tile_size, ud_list, "game", map)
                elif ev_button == 3:
                    mouse.mouseclickright(camera, screen, tile_size, ud_list, "game", grid, selectedObject)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and not lkeys[pygame.K_p]:
            creative = not creative
            if not creative:
                kActive = False
                lActive = False
                window.button_list = []
                window.image_list = []

        if keys[pygame.K_b] and not lkeys[pygame.K_b] and creative:
            debug = not debug
        if keys[pygame.K_r] and not lkeys[pygame.K_r] and creative:
            respawn = not respawn
        if keys[pygame.K_q] and not lkeys[pygame.K_q] and creative:
            grid.store(".\\data\\maps\\holibuli.gr")

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
            if keys[pygame.K_k] and not lkeys[pygame.K_k]:
                kActive = not kActive
                window.button_list = []
                window.image_list = []
                lActive = False
                if kActive:
                    for k in range(len(allObjects)):
                        window.addButton("selectObject:" + str(allObjects[k][0]), "", 30, (0, 255, 0), (tile_size * (0.5 + 2 * k), 100), 1.5 * tile_size, 1.5 * tile_size, (255, 255, 255))
                        window.addImage(bigSprite[allObjects[k][1]].image, (tile_size * (0.75 + 2 * k), 100 + 0.25 * tile_size))
            if keys[pygame.K_l] and not lkeys[pygame.K_l]:
                lActive = not lActive
                window.button_list = []
                window.image_list = []
                kActive = False
                if lActive:
                    for k in range(len(allBlocks)):
                        window.addButton("selectBlock:" + str(allBlocks[k][0]), "", 30, (0, 255, 0), (tile_size * (0.5 + 2 * k), 100), 1.5 * tile_size, 1.5 * tile_size, (255, 255, 255))
                        window.addImage(bigSprite[allBlocks[k][1]].image, (tile_size * (0.75 + 2 * k), 100 + 0.25 * tile_size))

        else:
            player.get_events(grid, lkeys)
            camera.xcen = player.x
            camera.ycen = player.y - 1.8

        # UPDATE

        if not creative:
            for thing in ud_list:
                thing.update(grid, ud_list)
            if player.dead(grid):
                if respawn:
                    death = player.deathcounter
                    crouch = player.isCrouching
                    wantstodecrouch = player.wantstodecrouch
                    hitbox = player.hitbox
                    player = player_module.Player(player.rx, player.ry)
                    player.deathcounter += death+1
                    player.isCrouching = crouch
                    player.wantstodecrouch = wantstodecrouch
                    player.hitbox = hitbox
                else:
                    return "death"
            for win_block in winblock.winblock_list:
                if player.collide(win_block):
                    return "win"
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
                if grid[column][row] == 7:
                    bigSprite["death_block"].draw(screen, camera.coords_to_screen(column, row + 1, screen))

        # draw the things in ud_list
        for thing in ud_list:
            thing.draw(screen, camera, bigSprite)

        # draw the player
        player.draw(screen, camera, bigSprite, debug)

        if debug:
            # draw grid lines using pygame line function
            for row in range(len(grid[0])):
                pygame.draw.line(screen, (255, 255, 255), camera.coords_to_screen(0, row, screen), camera.coords_to_screen(len(grid), row, screen))
            for column in range(len(grid)):
                pygame.draw.line(screen, (255, 255, 255), camera.coords_to_screen(column, 0, screen), camera.coords_to_screen(column, len(grid[0]), screen))
            # draw small point at player x/y
            pygame.draw.circle(screen, (255, 255, 255), camera.coords_to_screen(player.x, player.y, screen), 2)

        # update the death counter
        window.text_list = []
        window.addText("Deaths: " + str(player.deathcounter), (250, 0), 30, (255, 255, 255))
        window.draw()

        for event in window.getEvents():
            if event[1][:len("selectObject:")] == "selectObject:":
                selectedObject = int(event[1][len("selectObject:"):])
            if event[1][:len("selectBlock:")] == "selectBlock:":
                selectedBlock = int(event[1][len("selectBlock:"):])

        # update the screen
        pygame.display.update()
        pygame.time.Clock().tick(60)