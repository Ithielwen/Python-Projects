"""
Assignment: Week 6 - Jumper Game
Course: CSE210 Programming with Classes
Team: Methuselah
Author: Joel Jensen
Email: jen21092@byui.edu
"""

from Display import Display

class GameStatus:

  def __init__(self, display, word):
    self.game_display = display
    self.winning_word = word

  def _player_wins(self, guess, word):
    """returns true if guess matches word"""
    return str(guess) == str(word)
 

  def _player_loses(self, guesses_left):
    """losing condition returns true if """
    if guesses_left == 0:
      return True
    return False
      
  def isGameOver(self, guessed_word, correct_word, guesses_left):
    '''checks if the game is over'''
    if self._player_wins(guessed_word, correct_word):
      print(self.winning_word)
      print("YOU WIN!\n\n")
      return True
    elif self._player_loses(guesses_left):
      print(self.game_display.get_display_image())
      print("\nTHE JUMPER HAS HIT THE GROUND! GAME OVER!\n")
      print(f"The word was... {self.winning_word}\n\n")
      return True
    return False