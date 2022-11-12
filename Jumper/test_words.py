"""
##################################################################
# TEST CODE to validate words class. NOT part of project design! #
##################################################################

BYU-I CSE 210 - Programming with Classes
Week 6 - Jumper Game, Team Methuselah

test_words.py
Developer: Brennon Jacobson
Last Edited: 05/12/2022
"""
import pytest
from Words import words

''' 
METHODS TO TEST:
    __init__
    resetWordsList(new_words)
    appendWord(word)
    getSecretWord()
    getWordBank()
'''

# Test Word Banks
# linux_words = ['archive','applet','binary','checksum','client','directory','host','kernel','library','python','program','expression']
# sports_words = ['score', 'touchdown', 'basket', 'run', 'goal', 'foul', 'turnover', 'error', 'win', 'champion']


### Test Initialization
def test_default_init():
    linux_words = ['archive','applet','binary','checksum','client','directory','host','kernel','library','python','program','expression']
    print("Default Bank")
    print(linux_words)

    default_bank = words()
    init_bank = default_bank.getWordBank()
    print("INIT BANK")
    print(init_bank)

def test_custom_init():
    sports_words = ['score', 'touchdown', 'basket', 'run', 'goal', 'foul', 'turnover', 'error', 'win', 'champion']

    sports_bank = words(sports_words)
    assert sports_bank.getWordBank() == sports_words

### Test Append Word
def test_appendWord():
    sports_words = ['score', 'touchdown', 'basket', 'run', 'goal', 'foul', 'turnover', 'error', 'win', 'champion']

    sports_bank = words(sports_words)
    sports_bank.appendWord('playoffs')
    updated_sports_bank = sports_bank.getWordBank()
    assert 'playoffs' in updated_sports_bank

    default_bank = words()
    default_bank.appendWord('repository')
    updated_default_bank = default_bank.getWordBank()
    assert 'repository' in updated_default_bank

### Test Reset Words Lists
def test_resetWordsList():
    start_words = ['score', 'touchdown', 'basket', 'run', 'goal', 'foul', 'turnover', 'error', 'win', 'champion']

    test_new_words = ['Fedora','Redhat', 'Ubuntu', 'MLB', 'NBA', 'MLS', 'NFL']

    default_bank = words()
    assert default_bank.resetWordsList(test_new_words) == True
    reset_default_bank = default_bank.getWordBank()
    assert reset_default_bank == test_new_words

    sports_bank = words(start_words)
    assert sports_bank.resetWordsList(test_new_words) == True
    reset_sports_bank = sports_bank.getWordBank()
    assert reset_sports_bank == test_new_words

### Test Get Secret Word
def test_getSecretWord():
    custom_words = ['score', 'touchdown', 'basket', 'run', 'goal', 'foul', 'turnover', 'error', 'win', 'champion']
    
    default_bank = words()  
    default_secret = default_bank.getSecretWord()
    default_bank_end = default_bank.getWordBank()

    assert default_secret not in default_bank_end

    custom_bank = words(custom_words)
    custom_secret = custom_bank.getSecretWord()
    custom_bank_end = custom_bank.getWordBank()

    assert custom_secret not in custom_bank_end


#############################
### FIX ME: NEED TO TEST FOR

### Test words type string input validation

### Test out of words scenarios

### Test append type mismatch

### Test word list of extreme size

pytest.main(["-v", "--tb=line", "-rN", __file__])
