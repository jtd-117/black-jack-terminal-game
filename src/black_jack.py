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

# ---------------------------------------------------------------------------- #

class Deck(object):
    """
    An INTERFACE for a standard 52-card deck.
    """

    class Card(object):
        """
        An INTERFACE for a card from a standard 52-card deck.
        """

        def __init__(self, suite, rank):
            """
            Initialises a standard playing card.

            :Parameters:
                    - `suite`: the TYPE of card taken from the `suites` dictionary
                    - `rank`: the NUMBER of the card taken from the `ranks` dictionary
            """
            self.suite = suite
            self.rank = rank
            self.value = ranks[self.rank]
            self.image = symbols[self.rank]

        def __str__(self):
            """
            Prints out the rank & suite of the card.
            """
            return self.rank + ' of ' + self.suite

        def __init__(self):
            """
            Initialises a standard 52-card deck.
            """
            self.all_cards = []
            
    def new_deck(self):
        """
        Initialises & shuffles a new deck of cards.
        """

        # STEP 1: Create new deck
        print("\nCreating new deck...")
        for suite in suites.keys():
            for rank in ranks.keys():
                self.all_cards.append(self.Card(suite, rank))

        # STEP 2: Shuffle deck
        print("\nShuffling deck...")
        shuffle(self.all_cards)
        return self.all_cards

    def delete_deck(self):
        """
        Deletes a deck of cards.
        """

        print("\nResetting deck...")
        self.all_cards = []

# ---------------------------------------------------------------------------- #

class Players(Deck.Card):
    """
    Defines the user as a player.
    """

    # Activitaes if dealer's face-up card is an ACE
    insurance = None
    
    def __init__(self, bank = 1000):
        """
        Initialises the player.

        :Parameters:
                - `bank`: the INITIAL betting balance of the player
        """

        self.hand = []
        self.bank = bank
        self.bet = None
        self.card_sum = 0
    
    def add_card(self, Deck):
        """
        Adds a card to the player's hands.
        """
        
        # STEP 1: Need to add card to hand AND remove same card from deck
        self.hand.append(Deck.all_cards[0])
        Deck.all_cards.pop(0)
        
        # STEP 2: Need to update card sum
        # CASE 2A: Card is 'Ace'
        if self.hand[-1].rank == 'Ace':
                
            # CASE 2AI Value of 'Ace' is 1
            if self.card_sum + ACEVALUE2 > BLACKJACK:
                    self.card_sum += ACEVALUE1

            # CASE 2AII: Value of 'Ace' is 11
            else:
                    self.card_sum += ACEVALUE2
        
        # CASE 2B: Any other card
        else:
            self.card_sum += self.hand[-1].value

    def reset_hand(self):
        """
        Resets the hand of the player.
        """

        self.hand = []
        self.card_sum = 0

# ---------------------------------------------------------------------------- #

class Dealers(Players):
    """
    Defines a black-jack dealer.
    """

    def __init__(self):
        """
        Initialise the dealer attributes.
        """

        self.hand = []
        self.card_sum = 0

# ---------------------------------------------------------------------------- #

def place_bet(Players):
    """
    Player places betting amount.

    :Parameters:
        - `Players`: the user to play the game
    """

    # STEP 1: Need to indicate round number and avaliable funds
    print(f"                                      DEAL\n" + BORDER)
    print(f"\n--| Current balance: ${Players.bank} |--")

    # STEP 2: Need to ensure proper input of player bet
    while True:
        try:    
            Players.bet = int(input("\nEnter betting amount: $"))
        except:
            print(INVALID)
            continue
        else:   
            # CASE 2A: Player inputs funds exceeding balance
            if (Players.bet > Players.bank):
                print("\nINSUFFICIENT FUNDS.")
                continue

            # CASE 2B: Player inputs a zero or neagtive bet
            elif (Players.bet <= 0):
                print("\nYOUR NOT THAT POOR!")
                continue

            # CASE 2C: Player input is acceptable
            else:
                print("\nTRANSACTION ACCEPTED...\n\n" + BORDER)
                break
    
    # STEP 3: Need to adjust player account balance
    Players.bank -= Players.bet