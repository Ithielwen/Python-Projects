"""
Instructor: Bro. Parrish
Class: CSE210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 08 Greed Game
Student: Mark Hammer
Class: Cast
"""
# Import section
### don't think we need any imports in this one

class Cast:
    """A collection of minerals"""

    def __init__(self):
        """Constructs a new cast dictionary"""
        self._minerals = {}
        
    def add_mineral(self, group, mineral):
        """Adds a mineral to the given group"""
        if not group in self._minerals.keys():
            self._minerals[group] = []
            
        if not mineral in self._minerals[group]:
            self._minerals[group].append(mineral)

    def get_minerals(self, group):
        """Gets the minerals in the given group"""
        results = []
        if group in self._minerals.keys():
            results = self._minerals[group].copy()
        return results
    
    def get_all_minerals(self):
        """Gets all of the minerals in the cast"""
        results = []
        for group in self._minerals:
            results.extend(self._minerals[group])
        return results

    def get_first_mineral(self, group):
        """Gets the first mineral in the given group"""
        result = None
        if group in self._minerals.keys():
            result = self._minerals[group][0]
        return result

    def remove_mineral(self, group, mineral):
        """Removes a mineral from the given group."""
        if group in self._minerals:
            self._minerals[group].remove(mineral)