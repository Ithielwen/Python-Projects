"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Final Project
Student: Michael Coleman
"""

from game.scripting.action import Action

class Generator(Action):
    '''
    This is the parent class for anything that is to randomly create objects in the game
    '''
    def execute(self, cast, script):
        '''
        Randomly generates something in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        '''
        pass

    def get_velocity(self):
        pass

    def get_time_between(self):
        pass

    def update_velocities(self, new_velocity):
        pass

    def update_time_between(self, new_time_between):
        pass