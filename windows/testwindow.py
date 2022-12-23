import buttons
import pygame
import untils.windowbuilder

window = None
def init(bigSprite, screen, title_size, activewindow):
    global window
    window = untils.windowbuilder.WindowBuilder(screen)
    window.setBackground("background.jpg")

    window.addText("Hello World!", (0, 0), 50, (255, 255, 255))
    window.addText("How are you?", (0, 50), 25, (0, 255, 0))

    window.addButton("button1", "Menu", 25, (0, 0, 0), (100, 200), 25, 25, (255, 255, 255))

    return "show_test"

def show(bigSprite, screen, tile_size, activewindow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    global window
    window.draw()

    for event in window.getEvents():
        if event[0] == "button_right_click":
            activewindow = "menu"

    return activewindow
