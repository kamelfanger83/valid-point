import buttons
import pygame
import sprites

def show(bigSprite, screen, tile_size, activewindow):
    keys = pygame.key.get_pressed()

    """if keys[pygame.K_SPACE]:
        activewindow = "init_game"""

    bigSprite["menu"].draw(screen, (0, 0))

    pygame.display.update()
    pygame.time.Clock().tick(60)

    return activewindow
