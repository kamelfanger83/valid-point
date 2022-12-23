import buttons
import pygame
import sprites
import time

counter = None

def show(bigSprite, screen, tile_size, activewindow):
    global counter

    if counter == None:
        counter = time.time()

    if time.time() - counter < 3:
        bigSprite["death_screen"].draw(screen, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)
    else:
        counter = None
        return "show_menu"

    return activewindow
