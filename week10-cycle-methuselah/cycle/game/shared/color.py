"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Emma Hungrige
Class: Color
"""

class Color:
    """A color.
    
    Color's job is to hold and provide information about itself. Color has a few convenience
    methods for comparing and converting to a tuple.
    
    Attributes:
    _red (int): Red color
    _green (int): Green color
    _blue (int): Blue color
    _alpha (int): Alpha or opacity
    """

    def __init__(self, red, green, blue, alpha = 225):
        """Constructs a new color using the specified RGB and alpha values. The alpha value is
        the color's opacity.
        
        Arguments:
            red (int): Red color
            green (int): Green color
            blue (int): Blue color
            alpha (int): Alpha or opacity
        """

        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha
    
    def to_tuple(self):
        """Gets color as a tuple of four values RGB and alpha.
        
        Returns:
            Tuple(int, int, int, int): the color as a tuple.
        """
        
        return (self._red, self._green, self._blue, self._alpha)
