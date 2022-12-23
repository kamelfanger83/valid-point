import buttons
import pygame
import sprites

def main_menu(bigSprite, screen, tile_size, init_game, game_loop):
    for i in range(len(buttons.all_buttons)):
        if buttons.all_buttons[i].menu == "main_menu":
            buttons.button_list.append(buttons.all_buttons[i])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    buttons.all_buttons = []
                    init_game()
                    game_loop()

        bigSprite["menu"].draw(screen, (0, 0))

        for i in range(len(buttons.button_list)):
            buttons.button_list[i].draw(screen, bigSprite, tile_size)


        pygame.display.update()
        pygame.time.Clock().tick(60)