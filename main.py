# PLATFORMER GAME

import pygame
import world
import player as player_module
import camera as camera_module
import sprites
import gödi
import mouse
import spawner
import buttons
import sand
import windows.menuwindow
import windows.gamewindow
import windows.deathwindow

# initialize a fullscreen pygame window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Platformer Game")

tile_size = screen.get_width()/12

activewindow = "main_menu"

bigSprite = sprites.Sprites()

# load grid images
bigSprite.load_sprite(".\\sprites\\tile.jpg", 1, 1, tile_size, "tile")
bigSprite.load_sprite(".\\sprites\\sand.jpg", 1, 1, tile_size, "sand")
bigSprite.load_sprite(".\\sprites\\bg.jpg", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "bg")
bigSprite.load_sprite(".\\sprites\\death_screen.png", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "death_screen")
bigSprite.load_sprite(".\\sprites\\menu.png", screen.get_width()/tile_size, screen.get_height()/tile_size, tile_size, "menu")

def load():
    player_module.Player().load(tile_size, bigSprite)
    gödi.Gödi().load(tile_size, bigSprite)
    spawner.Spawner().load(tile_size, bigSprite)
    sand.Sand().load(tile_size, bigSprite)
    buttons.loadsprites(tile_size, bigSprite)

    #load buttons
    buttons.Button(0, 0, 0, "creative")
    buttons.Button(11, 2, 0, "creative")
    buttons.Button(2.5, 3, 1, "main_menu")
    buttons.Button(2.5, 4, 1, "main_menu")

load()

# Main loop for windows
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    if activewindow == "main_menu":
        activewindow = windows.menuwindow.main_menu(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "game":
        activewindow = windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, "jumpandgian")
    elif activewindow == "ingame":
        activewindow = windows.gamewindow.run(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "death":
        activewindow = windows.deathwindow.screen(bigSprite, screen, tile_size, activewindow)