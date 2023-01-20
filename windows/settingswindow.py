import buttons
import pygame
import utils.windowbuilder
import windows.gamewindow
import windows.settingswindow

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = utils.windowbuilder.WindowBuilder(screen)
    window.setBackground("menu.png")

    window.addText("Einstellungen:", (250, 380), 90, (255, 255, 255))
    window.addText("Bitte wähle eine Möglichkeit aus.", (250, 480), 30, (100, 255, 0))

    window.addButton("leader", "Spielsession eröffnen", 30, (0, 255, 0), (132, 537), 50, 320, (255, 255, 255))
    window.addButton("player", "Spielsession beitreten", 30, (0, 255, 0), (132, 600), 50, 320, (255, 255, 255))
    window.addButton("settings", "Einstellungen", 30, (0, 255, 0), (132, 663), 50, 320, (255, 255, 255))

def show(bigSprite, screen, tile_size, activewindow, musicplayer):
    global window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        window.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)