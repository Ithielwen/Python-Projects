"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 13 Frogger Game
Student: Emma Hungrige
"""

class Cast:
    """
    The responsibility of cast is to keep track of a collection of actors. It has methods for
    adding, removing, and getting them by a group name.

    Attributes:
        _actors (dict): dictionary of actors {key: group_name, value: a list of actors}
    """

    def __init__(self):
        """
        Constructs a new actor.
        Constructs a new zone.
        """
        
        self._actors = {}
        self._end_zones = {}
    
    def add_actor(self, group, actor):
        """
        Adds an actor to the given group.

        Arguments:
            group (string): the name of the group
            actor (actor): the actor to add
        """

        if not group in self._actors.keys():
            self._actors[group] = []
        
        if not actor in self._actors[group]:
            self._actors[group].append(actor)
    
    def add_zone(self, group, actor):
        """
        Adds a zone to the given group.

        Arguments:
            group (string): the name of the group
            actor (actor): the actor to add
        """

        if not group in self._end_zones.keys():
            self._end_zones[group] = []
        
        if not actor in self._end_zones[group]:
            self._end_zones[group].append(actor)

    def get_actors(self, group):
        """
        Gets the actors in the given group.

        Arguments:
            group (string): the name of the group

        Returns:
            list: the actors in the group
        """

        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_zones(self, group):
        """
        Gets the zones in the given group.

        Arguments:
            group (string): the name of the group

        Returns:
            list: the zones in the group
        """

        results = []
        if group in self._end_zones.keys():
            results = self._end_zones[group].copy()
        return results      

    def get_all_actors(self):
        """
        Gets all of the actors in the cast.

        Returns:
            list: all of the actors in the cast
        """

        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results
    
    def get_first_actor(self, group):
        """
        Gets the first actor in the group.

        Arguments:
            group (str): the name of the group
        
        Returns:
            list: the first actor in the group
        """

        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result
    
    def remove_actor(self, group, actor):
        """
        Removes an actor from the group.

        Arguments:
            group (str): the name of the group
            actor (actor): the actor to remove
        """

        if group in self._actors:
            self._actors[group].remove(actor)

    def remove_all_from_group(self, group):
        if group in self._actors.keys():
            for actor in self._actors[group]:
                self._actors[group].remove(actor)
    