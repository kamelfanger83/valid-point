import buttons
import pygame
import sprites
import time

def show(bigSprite, screen, tile_size, activewindow):
    start = time.time()

    while time.time() - start < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        bigSprite["death_screen"].draw(screen, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)

    return "show_menu"
