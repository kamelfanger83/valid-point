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
import object

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

def init(bigSprite, screen, tile_size, activewindow, maparg, musicplayer):
    global grid
    global player
    global ud_list
    global debug
    global respawn
    global creative
    global lkeys
    global x_y_previous
    global camera
    global map
    global window
    global lActive
    global kActive
    global teleport
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

    grid.load("./data/maps/"+map+".gr", tile_size, ud_list)

    player = player_module.Player(float(grid.metadata["respawn_point"][0]), float(grid.metadata["respawn_point"][1]))

    debug = False
    respawn = grid.metadata["respawn"] == "1"

    lkeys = pygame.key.get_pressed()

    x_y_previous = [-1, -1]

    player.rx = float(grid.metadata["respawn_point"][0])
    player.ry = float(grid.metadata["respawn_point"][1])

    player.speed = float(grid.metadata["speed"])

    player.crouch_speed = float(grid.metadata["crouch_speed"])

    player.x_hit = float(grid.metadata["hitbox"][0])
    player.y_hit = float(grid.metadata["hitbox"][1])
    player.hitbox = object.RectangularHitbox(player.x_hit, player.y_hit, 0.5)

    camera.xcen = player.x
    camera.ycen = player.y + player.y_hit

    creative = grid.metadata["creative"] == "1"

    player.invincible = grid.metadata["invincible"] == "1"

    kActive = False
    lActive = False

    teleport = False

    if (musicplayer.getSong() != grid.metadata["music"]):
        musicplayer.setSong(grid.metadata["music"])
        musicplayer.startMusic()

def show(bigSprite, screen, tile_size, activewindow, musicplayer):
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
    global teleport
    
    while True:
        for event in pygame.event.get():
            mouse_buttons_pressed = pygame.mouse.get_pressed(num_buttons=3)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif mouse_buttons_pressed[0] and teleport and creative and not kActive and not lActive:
                tm = camera.screen_to_coords(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)
                player.x = tm[0]
                player.y = tm[1]
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
        if keys[pygame.K_t] and not lkeys[pygame.K_t] and creative:
            teleport = not teleport
        if keys[pygame.K_q] and not lkeys[pygame.K_q] and creative:
            # set pygame window to not fullscreen so that we can give input
            pygame.display.set_mode((800, 600), pygame.RESIZABLE)
            name = input("Enter the name of the map: ")
            grid.store(name)
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        if keys[pygame.K_m]:
            return "menu"

        # player controls
        if creative:
            # get keys and move camera xcen and ycen with wasd or arrow keys

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                camera.ycen += creative_speed
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                camera.ycen -= creative_speed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                camera.xcen -= creative_speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                camera.xcen += creative_speed
            if keys[pygame.K_k] and not lkeys[pygame.K_k]:
                kActive = not kActive
                window.button_list = []
                window.image_list = []
                lActive = False
                if kActive:
                    for k in range(len(allObjects)):
                        window.addButton("selectObject:" + str(allObjects[k][0]), "", 30, (0, 255, 0), (tile_size/screen.get_width() * (0.5 + 2 * k), 0.1), 1.5 * tile_size/screen.get_width(), 1.5 * tile_size/screen.get_height(), (255, 255, 255))
                        window.addImage(bigSprite[allObjects[k][1]].image, (tile_size/screen.get_width() * (0.75 + 2 * k), 0.1 + 0.25 * tile_size/screen.get_height()))
            if keys[pygame.K_l] and not lkeys[pygame.K_l]:
                lActive = not lActive
                window.button_list = []
                window.image_list = []
                kActive = False
                if lActive:
                    for k in range(len(allBlocks)):
                        window.addButton("selectBlock:" + str(allBlocks[k][0]), "", 30, (0, 255, 0), (tile_size/screen.get_width() * (0.5 + 2 * k), 0.1), 1.5 * tile_size/screen.get_width(), 1.5 * tile_size/screen.get_height(), (255, 255, 255))
                        window.addImage(bigSprite[allBlocks[k][1]].image, (tile_size/screen.get_width() * (0.75 + 2 * k), 0.1 + 0.25 * tile_size/screen.get_height()))

        else:
            player.get_events(grid, lkeys)

            camera_width = screen.get_width() / tile_size
            camera_height = screen.get_height() / tile_size

            accept = 0.2

            camera.xcen = player.x

            if player.y + player.hitbox.half_height > camera.ycen + accept * camera_height:
                camera.ycen = player.y + player.hitbox.half_height - accept * camera_height
            elif player.y - player.hitbox.half_height < camera.ycen - accept * camera_height:
                camera.ycen = player.y - player.hitbox.half_height + accept * camera_height

        # UPDATE

        if not creative:
            for thing in ud_list:
                thing.update(grid, ud_list)
            if player.dead(grid):
                if respawn:
                    player.x = player.rx
                    player.y = player.ry
                    player.deathcounter += 1
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
            # display the mouses tile position
            window.text_list = []
            window.addText("Mouse: " + str(camera.screen_to_coords(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], screen)), (0.01, 0.05), 30, (255, 255, 255))
            window.draw()

        # update the death counter
        window.text_list = []
        window.addText("Deaths: " + str(player.deathcounter), (0.01, 0.01), 30, (255, 255, 255))
        window.draw()

        for event in window.getEvents():
            if event[1][:len("selectObject:")] == "selectObject:":
                selectedObject = int(event[1][len("selectObject:"):])
            if event[1][:len("selectBlock:")] == "selectBlock:":
                selectedBlock = int(event[1][len("selectBlock:"):])

        # update the screen
        pygame.display.update()
        pygame.time.Clock().tick(60)