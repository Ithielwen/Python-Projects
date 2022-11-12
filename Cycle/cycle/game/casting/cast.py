"""
Instructor: Bro. Parrish
Class: CSE 210
Semester: Spring 2022
Team: Methuselah
Assignment: Week 10 Cycle Game
Student: Brennon Jacobson
"""

class Cast:
    '''
    A collection of actors organized in a dictionary by group

    Attributes:
        _actors (DICT{key: group_name, value: LIST of actors}) 
    '''
    def __init__(self):
        self._actors = {}

    ##### ADD #####
    def add_actor(self, group, new_actor):
        '''
        Adds an actor to a group

        Args:
            group (STRING): key of dictionary, group name
            new_actor (ACTOR): actor object to add to a value list
        '''
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not new_actor in self._actors[group]:
            self._actors[group].append(new_actor)

    ##### REMOVE #####
    def remove_actor(self, group, del_actor):
        '''
        Remove an actor from a given group

        Args:
            group (STRING): key of dictionary, group name
            del_actor (ACTOR): actor object to remove from value list
        '''
        if group in self._actors:
            self._actors[group].remove(del_actor)

    ##### GETTERS #####
    def get_all_actors(self):
        '''
        Gets all of the actors in the dictionary
        
        Returns:
            LIST of all values in the actors dictonary (not group specific)
        '''
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_actor_by_group(self, group):
        '''
        Gets all of the actors in a given group

        Returns:
            LIST: list of actors in a given group
        '''
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results

    def get_first_actor(self, group):
        '''
        Gets the first actor in a given group

        Returns:
            ACTOR: first actor object in a group value list
        '''
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result