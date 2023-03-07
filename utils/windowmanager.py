import uuid
import pygame
import utils.musicplayer
class WindowManager:
    def __init__(self):
        pygame.init()
        self.windows = {}
        self.musicplayer = utils.musicplayer.Musicplayer()

    def getMusicplayer(self):
        return self.musicplayer

    def getWindows(self):
        return self.windows

    def existWindow(self, uuid):
        if uuid in self.windows:
            return True
        else:
            return False

    def removeWindow(self, uuid):
        if self.existWindow(uuid):
            del self.windows[uuid]

    def addWindow(self, window):
        id = uuid.uuid4().hex
        self.windows[id] = window

        return id

