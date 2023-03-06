# @file	    black_jack.py
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

# MISCELLANEOUS VARIABLES & LIBRARIES

from random import shuffle

INVALID = "\nINVALID INPUT."
BORDER = "# ---------------------------------------------------------------------------- #"

BROKE = 0
ACEVALUE1 = 1
ACEVALUE2 = 11
RISKYBOUNDARY = 17
BLACKJACK = 21

suites = {
    'Spades': '♠︎',
    'Clubs': '♣︎',
    'Hearts': '♥︎',
    'Diamonds': '♦︎'
}

ranks = {
    'Ace': (1,11),
    'Two': 2, 
    'Three': 3, 
    'Four': 4, 
    'Five': 5, 
    'Six': 6, 
    'Seven': 7, 
    'Eight': 8, 
    'Nine': 9, 
    'Ten': 10, 
    'Jack': 10, 
    'Queen':10, 
    'King': 10
}

symbols = {
    'Ace': 'A ', 
    'Two': '2 ', 
    'Three': '3 ', 
    'Four': '4 ', 
    'Five': '5 ', 
    'Six': '6 ', 
    'Seven': '7 ', 
    'Eight': '8 ', 
    'Nine': '9 ', 
    'Ten': '10', 
    'Jack': 'J ', 
    'Queen': 'Q ', 
    'King': 'K '
}

stand_hit = ['s','h']
yes_no = ['y','n']
