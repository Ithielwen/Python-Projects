"""
Instructor: Bro. Parrish
Semester: Spring 2022
Course: CSE210
Team: Methuselah
Author: Mark Hammer
Email: ham21019@byui.edu
"""

class UserInput:
    """
    This class defines the behavior for the user's input for the jumper game
    """

    def __init__(self):
        """initialize the class"""
        self._letters_guessed = []
        self._guessed_letter = ""

    def set_guess(self):
        """
        """
        guessed = True
        while guessed == True:
            guess = str(input("Please guess a letter: ")).lower()
            if self.has_guessed(guess):
                print(f"{guess} has aleady been guessed!\n")
            else:
                guessed = False
        
        self._guessed_letter = guess
        self._set_letters_guessed(guess)

        return guess

    def _set_letters_guessed(self, letter):
        self._letters_guessed.append(letter)

    def has_guessed(self, guess):
        """
        """
        if guess in self._letters_guessed:
            return True
        return False
