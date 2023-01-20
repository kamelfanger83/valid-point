from pygame import mixer

class Mussicplayer:
    def __init__(self):
        mixer.init()
        mixer.music.set_volume(100)
        self.song = ""

    def setVolume(self, volume):
        mixer.music.set_volume(volume)

    def getVolume(self):
        return mixer.music.get_volume()

    def setSong(self, filename):
        mixer.music.stop()
        mixer.music.load(filename)
        self.song = filename
    def getSong(self):
        return self.song

    def startMusic(self):
        mixer.music.play(loops=-1)

    def stopMusic(self):
        mixer.music.stop()

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()