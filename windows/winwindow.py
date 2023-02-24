import buttons
import pygame
import sprites
import time
import pygame
# import pyglet
import ctypes

def show(bigSprite, screen, tile_size, activewindow, musicplayer):
    """player = pyglet.media.Player()
    source = pyglet.media.load("./data/video/win.mp4")
    player.queue(source)
    player.play()

    pygame.display.flip()"""

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

            screen.fill(0)

       # player.dispatch_events()
       # tex = player.get_texture()
       # raw = tex.get_image_data().get_data('RGBA', tex.width * 4)
       # raw = ctypes.string_at(ctypes.addressof(raw), ctypes.sizeof(raw))
      #  img = pygame.image.frombuffer(raw, (tex.width, tex.height), 'RGBA')
       # screen.blit(img, (0, 0))

        pygame.display.flip()
