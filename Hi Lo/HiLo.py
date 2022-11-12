"""
BYU-I CSE 210 - Programming with Classes
Week 4 - HiLo Game, Team Methuselah

HiLo.py
Assigned: Emma Hungrige
Last Edited: 05/18/2022
"""

from Card import Card
from Deck import Deck
from Player import Player

#Variables

carddeck = Deck()
carddeck.shuffle()
human = Player()

#Gameplay Functions

def playagain():
    """Function to give user option to play the game again or end it
        
        Parameters: None
        Return: None
    """
    answer = input("Play again? Y or N \n").upper().strip()

    if answer == "Y" and human.points > 0:

        print("Okay!")
        playgame()

    elif answer == "N" or human.points <= 0:
        print("Thanks for playing!")
        endgame()

    else:
        print("INVALID ANSWER! GAME OVER!")
        endgame()

def endgame():
    """Function to end the program
        
        Parameters: None
        Return: None
    """

    print("GAME OVER! THANK YOU FOR PLAYING!")
    quit()

def playgame():
    """Function for gameplay 
    
        Parameters: None
        Return: None
    """
    if carddeck.nextCard.value == -1:
        card = carddeck.drawCard()
    else:
        card = carddeck.nextCard.value

    nextCard = carddeck.drawCard()
    carddeck.nextCard.value = nextCard

    points = human.points

    print(f"The current card is: {card}")
    
    guess = input("Guess H for high or L for low: \n").upper().strip()
    correct = human.guessCard(guess, card, nextCard)

    print(f"The next card was...{nextCard}")
    human.points = human.updateScore(correct, points)

    playagain()

def main():
    
    print("Welcome to HiLo! Let's get ready to rumble!")
    playgame()

if __name__ == "__main__":
    main()

#We've been trying to reach you about your car's extended warranty...
