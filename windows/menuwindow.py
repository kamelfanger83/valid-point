import buttons
import pygame
import untils.windowbuilder

window = None

def init(bigSprite, screen, title_size, activewindow):
    global window
    window = untils.windowbuilder.WindowBuilder(screen)
    window.setBackground("menu.png")

    window.addText("Menu:", (250, 380), 90, (255, 255, 255))
    window.addText("Bitte wähle eine Welt aus.", (250, 480), 30, (100, 255, 0))

    window.addButton("jumpandgian", "Jump and Run (Gian)", 30, (0, 255, 0), (132, 537), 50, 320, (255, 255, 255))
    window.addButton("test", "Testwelt (Linus)", 30, (0, 255, 0), (132, 600), 50, 320, (255, 255, 255))

def show(bigSprite, screen, tile_size, activewindow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    global window
    window.draw()

    for event in window.getEvents():
        if event[0] == "button_right_click":
            if(event[1] == "jumpandgian"):
                return "game"
            elif(event[1] == "test"):
                return "game"

    return activewindow
