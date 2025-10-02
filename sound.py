import pygame as pg
import zipfile
import io

class NoSound:
    def play(self, *args, **kwargs):
        pass
    def set_volume(self, *args, **kwargs):
        pass

class DummyMusic:
    def load(self, *args, **kwargs):
        pass
    def play(self, *args, **kwargs):
        pass
    def set_volume(self, *args, **kwargs):
        pass
    def stop(self, *args, **kwargs):
        pass

class Sound:
    def __init__(self, game):
        self.game = game
        try:
            pg.mixer.init()
            self.zip_archive = zipfile.ZipFile('resources.zip', 'r')
            self.path = 'resources/sound/'
            self.shotgun = self.load_sound('shotgun.wav')
            self.scorpion = self.load_sound('scorpion.wav')
            self.npc_pain = self.load_sound('npc_pain.wav')
            self.npc_death = self.load_sound('npc_death.wav')
            self.npc_shot = self.load_sound('npc_attack.wav')
            self.npc_shot.set_volume(0.2)
            self.player_pain = self.load_sound('player_pain.wav')
            self.load_music('theme.mp3')
            pg.mixer.music.set_volume(0.8)
        except pg.error:
            print("Warning: Could not initialize sound. Running in silent mode.")
            self.shotgun = NoSound()
            self.scorpion = NoSound()
            self.npc_pain = NoSound()
            self.npc_death = NoSound()
            self.npc_shot = NoSound()
            self.player_pain = NoSound()
            pg.mixer.music = DummyMusic()

    def load_sound(self, filename):
        sound_data = self.zip_archive.read(self.path + filename)
        return pg.mixer.Sound(file=io.BytesIO(sound_data))

    def load_music(self, filename):
        music_data = self.zip_archive.read(self.path + filename)
        pg.mixer.music.load(io.BytesIO(music_data))