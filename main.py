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
bigSprite.load_sprite(".\\sprites\\tile.jpg", 1, 1, tile_size, "tile")
bigSprite.load_sprite(".\\sprites\\sand.jpg", 1, 1, tile_size, "sand")
bigSprite.load_sprite(".\\sprites\\bg.jpg", sw/tile_size, sh/tile_size, tile_size, "bg")
bigSprite.load_sprite(".\\sprites\\death_screen.png", sw/tile_size, sh/tile_size, tile_size, "death_screen")
bigSprite.load_sprite(".\\sprites\\menu.png", sw/tile_size, sh/tile_size, tile_size, "menu")

menu = "main"

def load():
    player_module.Player().load(tile_size, bigSprite)
    gödi.Gödi().load(tile_size, bigSprite)
    spawner.Spawner().load(tile_size, bigSprite)
    sand.Sand().load(tile_size, bigSprite)
    buttons.Button(w=sw/4, h=sh/8, path=".\\sprites\\item_bg.jpg").load(tile_size, bigSprite)

load()

# Main loop for windows
while True:
    if activewindow == "menu":
        activewindow = windows.menuwindow.show(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "game":
        activewindow = windows.gamewindow.show(bigSprite, screen, tile_size, activewindow, "jumpandgian")
    elif activewindow == "death":
        activewindow = windows.deathwindow.show(bigSprite, screen, tile_size, activewindow)
    elif activewindow == "test":
        activewindow = windows.testwindow.show(bigSprite, screen, tile_size, activewindow)
