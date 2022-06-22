"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Mark Hammer
Class: Music
"""
from pyray import *
import pyray

class PlaySound:
    """this class handles the background music"""

    def __init__(self):
        """set the music file"""
        self._background_music = pyray.load_music_stream("greed/music/background_music.mp3")
        pyray.play_music_stream(self._background_music)

    def play_music(self):
        """plays music"""
        pyray.update_music_stream(self._background_music)