from pygame import mixer

class Mussicplayer:
    def __init__(self):
        mixer.init()
        mixer.music.set_volume(100)

    def setMusicFile(self, filename):
        mixer.music.load(filename)

    def startMusic(self):
        mixer.music.play(loops=-1)

    def stopMusic(self):
        mixer.music.stop()

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()