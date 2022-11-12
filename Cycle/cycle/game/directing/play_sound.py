"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Mark Hammer
"""

# Import section
import pyray

class PlaySound:
    """this class handles the background music"""

    def __init__(self):
        """set the music file"""
        self._background_music = pyray.load_music_stream("game/directing/background_music.mp3")
        pyray.play_music_stream(self._background_music)

    def play_music(self):
        """plays music"""
        pyray.update_music_stream(self._background_music)

    """
    code below is from Joel. If we want to play sound effects we can use the format and add the sound files
    """
    # def play_shing(self):
    #     shing = pyray.load_sound("greed/music/zapsplat_sound_design_fm_hit_sheen_shing_77785.mp3")
    #     pyray.play_sound(shing)

    # def play_hit(self):
    #     hit = pyray.load_sound("greed/music/zapsplat_sound_design_hit_impact_punchy_blow_77935.mp3")
    #     pyray.play_sound(hit)
