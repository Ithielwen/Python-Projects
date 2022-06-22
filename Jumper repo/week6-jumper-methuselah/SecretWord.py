"""
BYU-I CSE 210 - Programming with Classes
Week 6 - Jumper Game, Team Methuselah

SecretWord.py
Developer: Brennon Jacobson
Last Edited: 05/23/2022

ATTRIBUTES:
    _word 
    _correct_letters

METHODS:
    __init__ sets word
    isInWord(letter) bool

"""

class SecretWord:

    def __init__(self, secret_word):
        self._word = secret_word
        self._correct_letters = []

    def isInWord(self, letter):
        if letter in self._word:
            self._correct_letters.append(letter)
            print(f"\n{letter.upper()}, is in the word!")
            return True
        print(f"\n{letter.upper()}, is not in the word. Try again!")
        return False

    def __str__(self):
        word_display = ""
        for letter in self._word:
            if letter in self._correct_letters:
                word_display = word_display + letter
            else:
                word_display = word_display + " _ "
        
        return word_display
    