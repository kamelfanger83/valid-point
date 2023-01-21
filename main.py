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
import respawnpoint
import winblock
import windows.menuwindow
import windows.gamewindow
import windows.deathwindow
import windows.testwindow
import windows.winwindow
import windows.settingswindow
import utils.musicplayer

# initialize a fullscreen pygame window
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Platformer Game")

tile_size = screen.get_width() // 12

activewindow = "menu"

bigSprite = sprites.Sprites()

sw = screen.get_width()
sh = screen.get_height()

# load grid images
bigSprite.load_sprite("./data/img/tile.jpg", 1, 1, tile_size, "tile")
bigSprite.load_sprite("./data/img/sand.jpg", 1, 1, tile_size, "sand")
bigSprite.load_sprite("./data/img/bg.jpg", sw / tile_size, sh / tile_size, tile_size, "bg")
bigSprite.load_sprite("./data/img/death_screen.png", sw / tile_size, sh / tile_size, tile_size, "death_screen")
bigSprite.load_sprite("./data/img/win_screen.jpg", sw / tile_size, sh / tile_size, tile_size, "win_screen")
bigSprite.load_sprite("./data/img/menu.png", sw / tile_size, sh / tile_size, tile_size, "menu")
bigSprite.load_sprite("./data/img/death_block.jpg", 1, 1, tile_size, "death_block")

#init music player
musicplayer = utils.musicplayer.Mussicplayer()

menu = "main"


def load():
    player_module.Player().load(tile_size, bigSprite)
    gödi.Gödi().load(tile_size, bigSprite)
    spawner.Spawner().load(tile_size, bigSprite)
    sand.Sand().load(tile_size, bigSprite)
    respawnpoint.Respawnpoint().load(tile_size, bigSprite)
    winblock.Winblock().load(tile_size, bigSprite)
    buttons.Button(w=sw / 4, h=sh / 8, path="./data/img/item_bg.jpg").load(tile_size, bigSprite)
    bigSprite.load_sprite("./data/img/gödi.png", 1, 1, tile_size, "select_gödi")
    bigSprite.load_sprite("./data/img/spawner_idle.png", 1, 1, tile_size, "select_spawner")
    bigSprite.load_sprite("./data/img/respawnpoint.jpg", 1, 1, tile_size, "select_respawnpoint")
    bigSprite.load_sprite("./data/img/winblock.jpg", 1, 1, tile_size, "select_winblock")
    bigSprite.load_sprite("./data/img/sand.jpg", 0, 0, tile_size, "select_nothing")


load()

windows.menuwindow.init(bigSprite, screen, tile_size, activewindow)

while True:
    if activewindow == "menu":
        activewindow = windows.menuwindow.show(bigSprite, screen, tile_size, activewindow, musicplayer)
    elif activewindow == "settings":
        activewindow = windows.settingswindow.show(bigSprite, screen, tile_size, activewindow, musicplayer)
    elif activewindow == "game":
        activewindow = windows.gamewindow.show(bigSprite, screen, tile_size, activewindow, musicplayer)
    elif activewindow == "death":
        activewindow = windows.deathwindow.show(bigSprite, screen, tile_size, activewindow, musicplayer)
    elif activewindow == "win":
        activewindow = windows.winwindow.show(bigSprite, screen, tile_size, activewindow, musicplayer)
    elif activewindow == "create":
        activewindow = windows.worldselector.show(bigSprite, screen, tile_size, activewindow, musicplayer)