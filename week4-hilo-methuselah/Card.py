"""
Author: Mark Hammer

Class Plan:

class Card(object):
    #def __init__(REPLACE):

    #def __gt__(REPLACE) (greather than):

    #def __lt__(REPLACE) (less than):

    #def show(REPLACE):
"""

class Card:
    """create Card class for use in Hi-Lo card game
    """

    def __init__(self, value):
    
        self.value = value
    
    def __gt__(self, comp_card):
        """define a function for overloading operator greater than ">"
        should return a bolean value
        """
        winner = self.value > comp_card
        return winner
    
    def __lt__(self, comp_card):
        """define a function for overloading operator less than "<"
        should return a bolean value
        """
        loser = self.value < comp_card
        return loser

    def show(self):
        """displays the card
        """
        print(f"The card you drew is: {self.value}")