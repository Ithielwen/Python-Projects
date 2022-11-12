"""
BYU-I CSE 210 - Programming with Classes
Week 6 - Jumper Game, Team Methuselah

Jumper.py
Assigned: Emma Hungrige
Last Edited: 05/23/2022
"""

from Words import words
from GameStatus import GameStatus
from Display import Display
from user_input import UserInput
from SecretWord import SecretWord


def main():
  #Set up game play
  word_list = words()
  new_word = word_list.getSecretWord() #1. The puzzle is a secret word randomly chosen from a list.
  secret_word = SecretWord(new_word) 
  game_display = Display()
  game_status = GameStatus(game_display, new_word)
  usr_input = UserInput()

  game_over = False

  print("Let's play Jumper! Guess all the letters in the word correctly before the jumper hits the ground!")

  while game_over == False:
    #2. The player guesses a letter in the puzzle.
    print(game_display.get_display_image())
    print(secret_word)
    # print(f"\nWORD IS: {new_word}") #Print for bug testing

    this_guess = usr_input.set_guess() #.set_guess checks if already guessed

    #3. If the guess is correct, the letter is revealed.
    if secret_word.isInWord(this_guess) == False: #number 3 automatically added encapsulated in the isInWord function
      #4. If the guess is incorrect, a line is cut on the player's parachute.
      game_display.add_incorrect_letter()
    
    #5. If the puzzle is solved the game is over.
    #6. If the player has no more parachute the game is over.
    guesses_left = game_display.get_guesses_left()
    game_over = game_status.isGameOver(secret_word, new_word, guesses_left)

if __name__ == "__main__":
  main()




