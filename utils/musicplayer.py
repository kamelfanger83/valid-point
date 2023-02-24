from pygame import mixer

class Mussicplayer:
    def __init__(self):
        mixer.init()
        mixer.Channel(0).set_volume(100)
        mixer.Channel(1).set_volume(0)

        self.song = ""
        self.volume = 100
        self.active = 0

    def setVolume(self, volume):
        mixer.Channel(self.active).set_volume(volume)
        self.volume = volume

    def getVolume(self):
        return self.volume

    def setSong(self, filename):
        channel = 0

        if self.active == 0:
            channel = 1

        mixer.Channel(channel).stop()
        mixer.Channel(channel).play(mixer.Sound(filename), -1)
        mixer.Channel(channel).pause()

        self.song = filename
    def getSong(self):
        return self.song

    def startMusic(self):
        channel = 0

        if self.active == 0:
            channel = 1

        mixer.Channel(channel).unpause()
        mixer.Channel(self.active).fadeout(1000)

        self.active = channel

    def stopMusic(self):
        mixer.Channel(self.active).stop()

    def pauseMusic(self):
        mixer.Channel(self.active).pause()

    def unpauseMusic(self):
        mixer.Channel(self.active).unpause()