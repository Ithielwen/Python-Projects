"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Emma Hungrige
Class: Point
"""

class Point:
    """A distance from a relative origin (0, 0)
    
    Point's job is to hold and provide information about itself. Point has a few convenience
    methods for adding, scaling, and comparing.

    Attributes:
        _x (int): horizontal axis
        _y (int): vertical axis
    """

    def __init__(self, x, y):
        """Constructs a new point using the specified x and y values.
        
        Arguments:
            x (int): x value
            y (int): y value
        """

        self._x = x
        self._y = y
    
    def add(self, other):
        """Gets a new point that is the sum of this and the given point.
        
        Arguments:
            other (Point): the point to add
        
        Returns:
            Point: new point that is the sum
        """

        x = self._x + other.get_x()
        y = self._y + other.get_y()

        return Point(x, y)
    
    def equals(self, other):
        """Whether or not this point is equal to the given one.

        Arguments:
            other (Point): the point to compare

        Returns:
            boolean: True if x = y; false if otherwise
        """

        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            int: horizontal distance
        """

        return self._x
    
    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            int: vertical distance
        """

        return self._y
    
    def reverse(self):
        """Reverses the point by inverting both x and y values.
        
        Returns:
            point: new reversed point
        """

        new_x = self._x * -1
        new_y = self._y * -1

        return Point(new_x, new_y)

    def scale(self, factor):
        """Scales the point by the provided factor.
        
        Arguments:
            factor (int): amount to scale
            
        Returns:
            point: new scaled point
        """

        return Point(self._x * factor, self._y * factor)