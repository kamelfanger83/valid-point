import buttons
import pygame
import utils.windowbuilder
import windows.gamewindow
import windows.settingswindow
import os

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = utils.windowbuilder.WindowBuilder(screen)
    window.setBackground("menu.png")

    window.addText("Menu:", (250, 380), 90, (255, 255, 255))
    window.addText("Bitte wähle eine Welt aus.", (250, 480), 30, (100, 255, 0))

    # go through files in ./data/maps and add buttons for each

    directory = os.fsencode("./data/maps")

    i = 0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # mapname is first column of map file
        mapname = open("./data/maps/" + filename, "r").readline()[:-1]
        if filename.endswith(".gr"):
            window.addButton(filename, mapname, 30, (0, 255, 0), (132, 537 + i * 63), 50, 320, (255, 255, 255))
            i += 1
        else:
            continue


def show(bigSprite, screen, tile_size, activewindow, musicplayer):
    # Music
    if(musicplayer.getSong() != "./data/music/menu.wav"):
        musicplayer.setSong("./data/music/menu.wav")
        musicplayer.startMusic()

    global window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        window.draw()

        for event in window.getEvents():
            if event[0] == "button_right_click":
                windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, event[1][:-3])
                return "game"

        pygame.display.update()
        pygame.time.Clock().tick(60)