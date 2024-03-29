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

    window.addText("Menu:", (0.1, 0.1), screen.get_height() // 11, (255, 255, 255))
    window.addText("Bitte wähle eine Möglichkeit aus.", (0.15, 0.2), 30, (100, 255, 0))
    # go through files in ./data/maps and add buttons for each
    # 5 buttons per column

    directory = os.fsencode("./data/maps")

    i = 0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # mapname is first column of map file
        mapname = open("./data/maps/" + filename, "r").readline()[:-1]
        if filename.endswith(".gr"):
            column = i // 5
            row = i % 5
            window.addButton(filename, mapname, 30, (0, 255, 0), (0.2 + 0.2 * column, 0.5 + 0.1 * row), 0.19, 0.09, (255, 255, 255))
            i += 1
        else:
            continue


def show(bigSprite, screen, tile_size, activewindow, musicplayer):

    pygame.mouse.set_visible(True)

    # Music
    if(musicplayer.getSong() != "./data/music/menu.wav"):
        musicplayer.setSong("./data/music/menu.wav")
        musicplayer.startMusic()

    global window

    newMousePress = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        window.draw()

        mouseUp = True
        for event in window.getEvents():
            if event[0] == "left_click":
                mouseUp = False
                if (newMousePress):
                    windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, event[1][:-3], musicplayer)
                    return "game"
        if (mouseUp):
            newMousePress = True

        pygame.display.update()
        pygame.time.Clock().tick(60)