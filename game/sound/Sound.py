from random import randint

import pygame


class Sound:
    def __init__(self):
        print("Init Sound class...")
        self.BLOCKS_SOUND = {}
        self.SOUNDS = {}
        self.MUSIC = []
        self.music_already_playing = False
        self.musicPlayer = pygame.mixer.music

        self.volume = 0.1

    def initMusic(self):
        musicNum = randint(0, len(self.MUSIC) - 1)
        self.musicPlayer.load(self.MUSIC[musicNum])
        for i in range(len(self.MUSIC)):
            if i == musicNum:
                continue
            self.musicPlayer.queue(self.MUSIC[i])

    def playSound(self, name, volume):
        channel = self.SOUNDS[name].play()
        channel.set_volume(volume)

    def playMusic(self):
        if self.music_already_playing:
            return
        if randint(0, 5000) == 746:
            self.music_already_playing = True
            self.musicPlayer.play(0, 0.1)
            self.musicPlayer.set_volume(self.volume)