"""
BYU-I CSE 210 - Programming with Classes
Week 6 - Jumper Game, Team Methuselah

words.py
Developer: Brennon Jacobson
Last Edited: 05/12/2022

ATTRIBUTES:
    _words 

METHODS:
    _shuffleWords(words_list, num_shuffles)
    resetWordsList(self, new_words)
    appendWord(self, word)
    getSecretWord(self)

"""
import random

class words:
    '''
    This class maintains a word bank for the use in word based games
    '''

    # establish a default words bank
    linux_words = ['archive','applet','binary','checksum','client','directory','host','kernel','library','python','program','expression']

    def __init__(self, words:list = linux_words):
        self._words = words

    def __str__(self):
        return str(self._words)

    def _shuffleWords(self, words_list, num_shuffles = 3):
        for times in range(0, num_shuffles):
            random.shuffle(words_list)

    def resetWordsList(self, new_words: list):
        '''
        This method sets the words list to a new user defined words list

        Parameters:
            new_words // an array to populate the word list
        Return:
            True // if new_words set successfully
            False // if new_words was not reset successfully
        '''
        self._words = new_words

        if self._words == new_words:
            return True
        else:
            return False
    
    def appendWord(self, word: str):
        '''
        This method appends a single word to the existing word list

        Parameters:
            word string // word to append

        Return:
            num_words // number of wrods in word bank
        '''
        self._words.append(word)

        return len(self._words)

    def getSecretWord(self):
        '''
        This method returns one secret word from the word bank by shuffling the word bank
        and popping the top word off to ensure no repeats

        Parameters:
            None

        Return:
            secret_word string
        '''
        word_bank = self._words
        self._shuffleWords(word_bank, 5)

        secret_word = word_bank.pop()
        return secret_word.lower().strip()


    def getWordBank(self):
        '''
        This method returns the complete word bank in list form
        '''
        return self._words
