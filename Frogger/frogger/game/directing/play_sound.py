"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Mark Hammer
"""

# Import section
import pyray

class PlaySound:
    """this class handles the background music"""

    def __init__(self):
        """set the music file for the background music to start the game"""
        # self._background_music = pyray.load_music_stream("./frogger/game/directing/sound-frogger-coin-in.wav")
        # pyray.play_music_stream(self._background_music)

    def play_music(self):
        """plays background music to start the game"""
        # pyray.update_music_stream(self._background_music)

    def play_coin_in(self):
        """plays coin in sound"""
        coin_in = pyray.load_sound("./frogger/game/directing/sound-frogger-coin-in.wav")
        pyray.play_sound(coin_in)

    def play_extra(self):
        """plays extra life sound"""
        extra = pyray.load_sound("./frogger/game/directing/sound-frogger-extra.wav")
        pyray.play_sound(extra)

    def play_hop(self):
        """plays hop sound"""
        hop = pyray.load_sound("./frogger/game/directing/sound-frogger-hop.wav")
        pyray.play_sound(hop)

    def play_plunk(self):
        """plays plunk sound when frog drowns"""
        plunk = pyray.load_sound("./frogger/game/directing/sound-frogger-plunk.wav")
        pyray.play_sound(plunk)

    def play_squash(self):
        """plays death sound when frog run over"""
        squash = pyray.load_sound("./frogger/game/directing/sound-frogger-squash.wav")
        pyray.play_sound(squash)