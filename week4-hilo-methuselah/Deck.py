'''
BYU-I CSE 210 - Programming with Classes
Week 4 - HiLo Game, Team Methuselah

Deck.py 
assigned: Brennon Jacobson, Michael Coleman
Last Edited: 05/06/2022
'''
import random
from Card import Card

class Deck:
    '''
    This class defines a Deck of Cards, four suites of 1 - 13.
    This takes option parameters of num of suits (dafault is traditional 4: Spades, Clubs, Diamonds, Hearts)
    Another optional paramenter is num_cards which is number of cards per suit (default is traiditional 13: Ace[1] through King[13])
    '''
    def __init__(self, num_suits = 4, num_cards = 13):
        self.cards = []
        self.build(num_suits, num_cards)

    # def __str__(self):
    #     '''This method prints the deck in the form of a list of cards for testing'''
    #     card_values = []
    #     for card in self.cards:
    #         card_values.append(card.value)

    #     return str(card_values)

    def build(self, num_suits, num_cards):
        '''This method is used to create a deck of cards. num_suits is the number of suits in a deck. num_cards is the number of cards in a suit.'''
        num_cards += 1 #Add 1 to account for card values not starting at 0

        for suit in range(num_suits):
            for card_value in range(1, num_cards):
                self.cards.append(Card(card_value))
        
    def shuffle(self, num_shuffles = 1):
        '''This method is used to shuffle the deck and takes an optional parameter of number of shuffles. Default is 1'''
        for times in range(0, num_shuffles):
            random.shuffle(self.cards)
    
    def show(self):
        '''This method prints the deck in the form of a list of cards for testing'''
        card_values = []
        for card in self.cards:
            card_values.append(card.show())

        return str(card_values)

    def drawCard(self):
        '''This method is used to return a card from the "top of the deck," then remove that card so it isn't drawn again.'''
        card_to_draw = self.cards.pop(0)
        return card_to_draw.value


### TEMP MAIN for Deck Class testing
def main():
    print("1) INITIALIZING DECK...")
    myDeck = Deck()
    
    print("Deck:")
    print(myDeck)
    
    ### Uncomment after shuffle() implemented for testing
    print("\n2) SHUFFLING DECK...")
    myDeck.shuffle()
    print("Shuffled:")
    print(myDeck)

    ### Uncomment after show() implemented for testing
    print("\n3) SHOW...")
    print(myDeck.show())
    
    ### Uncomment after draw() implemented for testing
    print("\n4) DRAW...")
    draw = myDeck.drawCard()
    print(f"You drew {draw}")

if __name__ == "__main__":
    main()