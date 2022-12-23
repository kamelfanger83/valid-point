import buttons
import pygame
import sprites

def show(bigSprite, screen, tile_size, activewindow):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            return "game"
        elif keys[pygame.K_RETURN]:
            return "init_test"

        bigSprite["menu"].draw(screen, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)

