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

    window.addText("Menu:", (250, 380), 90, (255, 255, 255))
    window.addText("Bitte wähle eine Möglichkeit aus.", (250, 480), 30, (100, 255, 0))

    window.addButton("leader", "Spielsession eröffnen", 30, (0, 255, 0), (132, 537), 50, 320, (255, 255, 255))
    window.addButton("player", "Spielsession beitreten", 30, (0, 255, 0), (132, 600), 50, 320, (255, 255, 255))
    window.addButton("settings", "Einstellungen", 30, (0, 255, 0), (132, 663), 50, 320, (255, 255, 255))

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
                if(event[1] == "leader"):
                    windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, "jumpandgian")
                    return "create"
                elif(event[1] == "player"):
                    windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, "test")
                    return "join"
                elif(event[1] == "settings"):
                    windows.settingswindow.init(bigSprite, screen, tile_size, activewindow)
                    return "settings"

        pygame.display.update()
        pygame.time.Clock().tick(60)