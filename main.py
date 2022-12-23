# PLATFORMER GAME

import pygame
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
import windows.testwindow

# initialize a fullscreen pygame window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Platformer Game")

tile_size = screen.get_width()//12

activewindow = "menu"

bigSprite = sprites.Sprites()

sw = screen.get_width()
sh = screen.get_height()

# load grid images
bigSprite.load_sprite(".\\data\\img\\tile.jpg", 1, 1, tile_size, "tile")
bigSprite.load_sprite(".\\data\\img\\sand.jpg", 1, 1, tile_size, "sand")
bigSprite.load_sprite(".\\data\\img\\bg.jpg", sw/tile_size, sh/tile_size, tile_size, "bg")
bigSprite.load_sprite(".\\data\\img\\death_screen.png", sw/tile_size, sh/tile_size, tile_size, "death_screen")
bigSprite.load_sprite(".\\data\\img\\menu.png", sw/tile_size, sh/tile_size, tile_size, "menu")

menu = "main"

def load():
    player_module.Player().load(tile_size, bigSprite)
    gödi.Gödi().load(tile_size, bigSprite)
    spawner.Spawner().load(tile_size, bigSprite)
    sand.Sand().load(tile_size, bigSprite)
    buttons.Button(w=sw/4, h=sh/8, path=".\\data\\img\\item_bg.jpg").load(tile_size, bigSprite)

load()

# Main loop for windows
while True:
    if activewindow == "menu":
        activewindow = windows.menuwindow.show(bigSprite, screen, tile_size, activewindow)
    elif str(activewindow).startswith("init_game_"):
        activewindow = windows.gamewindow.init(bigSprite, screen, tile_size, activewindow, activewindow.replace("init_game_", ""))
    elif activewindow == "show_game":
        activewindow = windows.gamewindow.show(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "show_death":
        activewindow = windows.deathwindow.show(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "init_test":
        activewindow = windows.testwindow.init(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "show_test":
        activewindow = windows.testwindow.show(bigSprite, screen, tile_size, activewindow)