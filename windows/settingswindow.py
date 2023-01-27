import buttons
import pygame
import utils.windowbuilder
import windows.gamewindow
import windows.settingswindow
import time

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = utils.windowbuilder.WindowBuilder(screen)
    window.setBackground("menu.png")

    window.addText("Einstellungen:", (0.25, 0.38), 90, (255, 255, 255))
    window.addText("Ändere die Einstellungen wie du willst:", (0.25, 0.48), 30, (100, 255, 0))

    window.addButton("music", "Musik an/ausschalten", 30, (0, 255, 0), (0.132, 0.537), 0.05, 0.0320, (255, 255, 255))
    window.addButton("player", "Spielsession beitreten", 30, (0, 255, 0), (0.132, 0.600), 0.05, 0.0320, (255, 255, 255))
    window.addButton("back", "Zurück", 30, (0, 255, 0), (0.132, 0.663), 0.5, 0.0320, (255, 255, 255))

def show(bigSprite, screen, tile_size, activewindow, musicplayer):
    global window
    while True:
        start = time.time()

        while time.time() - start < 0.1:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            pygame.display.update()
            pygame.time.Clock().tick(60)

        window.draw()

        for event in window.getEvents():
            if event[0] == "left_click":
                if (event[1] == "music"):
                    if(musicplayer.getVolume() > 0):
                        musicplayer.setVolume(0)
                    else:
                        musicplayer.setVolume(100)
                elif (event[1] == "player"):
                    windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, "jumpandgian")

                    if (musicplayer.getSong() != "./data/music/jumpandgian.wav"):
                        musicplayer.setSong("./data/music/jumpandgian.wav")
                        musicplayer.startMusic()

                    return "game"
                elif (event[1] == "back"):
                    windows.menuwindow.init(bigSprite, screen, tile_size, activewindow)
                    return "menu"

        pygame.display.update()
        pygame.time.Clock().tick(60)