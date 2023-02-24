import buttons
import pygame
import utils.windowbuilder
import windows.gamewindow
import windows.settingswindow
import windows.worldselector

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = utils.windowbuilder.WindowBuilder(screen)
    window.setBackground("bg.jpg")

    window.addText("Sever selector:", (0.1, 0.1), screen.get_height()//11, (255, 255, 255))
    window.addText("pliplis enter the ip address: ", (0.15, 0.2), 30, (100, 255, 0))
    window.addText("", (0.5, 0.2), 30, (100, 255, 0))

    # ten buttons for the numbers, a button for the dot and a button for finish
    # arranged in the same way as on a numpad
    for i in range(0, 10):
        window.addButton(str(i), str(i), 30, (0, 255, 0), (0.2 + 0.1 * (i % 3), 0.5 + 0.1 * (i // 3)), 0.05, 0.05, (255, 255, 255))
    window.addButton(".", ".", 30, (0, 255, 0), (0.3, 0.8), 0.05, 0.05, (255, 255, 255))
    window.addButton("finish", "finish", 30, (0, 255, 0), (0.4, 0.8), 0.1, 0.05, (255, 255, 255))

def show(bigSprite, screen, tile_size, activewindow, musicplayer):

    pygame.mouse.set_visible(True)

    # Music
    if(musicplayer.getSong() != "./data/music/menu.wav"):
        musicplayer.setSong("./data/music/menu.wav")
        musicplayer.startMusic()

    global window

    ip = []
    newMousePress = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        window.draw()

        mouseUp = True
        # the buttons can be used to enter the ip address
        for event in window.getEvents():
            # add the number to the ip address
            mouseUp = False;
            if event[0] == "left_click" and newMousePress:
                # when the finish button is pressed break out of while loop
                if event[1] == "finish":
                    return "menu"
                window.removeText("".join(ip), (0.5, 0.2))
                ip.append(event[1])
                window.addText("".join(ip), (0.5, 0.2), 30, (100, 255, 0))
                newMousePress = False
        if (mouseUp):
            newMousePress = True

        window.draw()

        pygame.display.update()
        pygame.time.Clock().tick(60)
