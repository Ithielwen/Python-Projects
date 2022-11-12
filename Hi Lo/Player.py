class Player:
    """
    BYU-I CSE 210 - Programming with Classes
    Week 4 - HiLo Game, Team Methuselah

    Player.py
    Assigned: Joel Jensen
    Last Edited: 05/10/2022

    This class defines the actions of the player for the Hi-Lo game. It contains methods for adding a username, drawing and displaying a card, and updating the player's score.
    
    Attributes:
        username: stores the name of the player
        points: stores the user's score, default is 300

    Methods:
        getName
        displayName
        draw
        show
        guessCard
        updateScore
        checkScore
        keepPlaying 
    """
    def __init__(self, username = "Player 1", points = 300):
        # Attributes
        self.username = username
        self.points = points
        # self.cardhand = cardhand


    def getName(self):
        """Use the getName method if you want the user to select a username.
        
            Parameters: None
            Return: None
        """
        self.username = input("What is your name? ")


    def displayName(self):
        """This method displays the username to the console.
                
            Parameters: None
            Return: None
        """
        print(f"\nHello {self.username}! Let's play Hi-Lo!\n")


    def draw(self, cards):
        """This method takes a card list comprising numeric values and returns one card value.
            Parameters:
                cards: a list with card values
            Return:
                cardhand: the value of one card from the list
        """
        # CARD_INDEX = random.choice(cards)
        # cardhand = cards.index(CARD_INDEX)
        cardhand = cards[0]
        return cardhand


    def show(self, cardhand):
        """This method displays the card selected by the user to the console.
            Parameters:
                cardhand: a value representing a card held by the user
            Return: None
        """
        print(f"Your card is {cardhand}.")


    def guessCard(self, guessed, cardhand, cardstack):
        """This method takes the user's guess and the card values. It returns True if the user guessed correctly and False if they guessed incorrectly.
            Parameters:
                guessed: a string with the user's guess
                cardhand: a value representing card held by user
                cardstack: a value representing card taken from deck
            Return:
                Boolean value determined by user's guess, True if correct, False if incorrect
        """
        while guessed[0].lower() != "h" and guessed[0].lower() != "l":
            guessed = input("Please enter (H/L): ")
            
        guess = guessed[0].lower()

        if guess == "h":
            return False if cardhand > cardstack else True
        elif guess == "l":
            return False if cardstack > cardhand else True


    def updateScore(self, guess, score):
        """This method updates the user's score based on their guess, whether correct or incorrect.
            Parameters:
                guess: boolean value, True if user guessed correctly, otherwise False
                score: int value representing user's current score
            Return:
                score: updates user's score
        """
        if guess:
            score += 100
            print("\n\t+100 points\n")
            self.checkScore(score)
        else:
            score -= 75
            print("\n\t-75 points\n")
            self.checkScore(score)
        return score


    def checkScore(self, score):
        """This method checks to see if the user has any remaining points to keep playing.
            Parameters:
                score: int value representing user's current score
            Return:
                None
        """
        if score > 0:
            print(f"Your current score is: {score}.")
        else:
            print(f"You have no more points left. Game Over!")
            quit()

    def keepPlaying(self, score):
        """If the user still has points this method asks them if they wish to continue playing.
            Parameters:
                score: int value representing user's current score
            Return:
                keepPlaying: string representing user's response to keep playing returns 'y' or 'n' 
        """
        if score > 0:
            keepPlaying = input("Do you want to keep playing (y/n)? ")
        return keepPlaying[0].lower()