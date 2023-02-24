import buttons
import pygame
import utils.windowbuilder
import windows.gamewindow
import windows.settingswindow
import windows.serverselectorwindow
import windows.worldselector

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = utils.windowbuilder.WindowBuilder(screen)
    window.setBackground("menu.png")

    window.addText("Menu:", (0.1, 0.1), screen.get_height()//11, (255, 255, 255))
    window.addText("Bitte wähle eine Möglichkeit aus.", (0.15, 0.2), 30, (100, 255, 0))

    window.addButton("leader", "Spielsession eröffnen", 30, (0, 255, 0), (0.2, 0.5), 0.3, 0.09, (255, 255, 255))
    window.addButton("player", "Spielsession beitreten", 30, (0, 255, 0), (0.2, 0.6), 0.3, 0.09, (255, 255, 255))
    window.addButton("settings", "Einstellungen", 30, (0, 255, 0), (0.2, 0.7), 0.3, 0.09, (255, 255, 255))


def show(bigSprite, screen, tile_size, activewindow, musicplayer):

    pygame.mouse.set_visible(True)

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
            if event[0] == "left_click":
                if(event[1] == "leader"):
                    windows.worldselector.init(bigSprite, screen, tile_size, activewindow)
                    return "create"
                elif(event[1] == "player"):
                    windows.serverselectorwindow.init(bigSprite, screen, tile_size, activewindow)
                    return "join"
                elif(event[1] == "settings"):
                    windows.settingswindow.init(bigSprite, screen, tile_size, activewindow)
                    return "settings"

        pygame.display.update()
        pygame.time.Clock().tick(60)