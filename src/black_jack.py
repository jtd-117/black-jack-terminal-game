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

class Player(Deck.Card):
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

class Dealer(Player):
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

def place_bet(player):
    """
    Player places betting amount.

    :Parameters:
        - `player`: an instance of the `Player` class
    """

    # STEP 1: Need to indicate round number and avaliable funds
    print(f"                                      DEAL\n" + BORDER)
    print(f"\n--| Current balance: ${player.bank} |--")

    # STEP 2: Need to ensure proper input of player bet
    while True:
        try:    
            player.bet = int(input("\nEnter betting amount: $"))
        except:
            print(INVALID)
            continue
        else:   
            # CASE 2A: Player inputs funds exceeding balance
            if (player.bet > player.bank):
                print("\nINSUFFICIENT FUNDS.")
                continue

            # CASE 2B: Player inputs a zero or neagtive bet
            elif (player.bet <= 0):
                print("\nYOUR NOT THAT POOR!")
                continue

            # CASE 2C: Player input is acceptable
            else:
                print("\nTRANSACTION ACCEPTED...\n\n" + BORDER)
                break
    
    # STEP 3: Need to adjust player account balance
    player.bank -= player.bet

# ---------------------------------------------------------------------------- #

def display_table(player, dealer, turn):
    """
    Display the cards of the dealer & player.

    :Parameters:
        - `player`: an instance of the `Player` class
        - `dealer`: an instance of the 'Dealer' class
        - `turn`: a boolean where 'True' represents Player turn & 'False' for the dealer
    """
    
    # STEP 1: Initialise the player & dealer cards
    player_cards = ['' for i in range(10)]
    dealer_cards = ['' for i in range(10)]
    dealer_first_card = True

    # STEP 2: Print the player's cards
    for card in player.hand:
        player_cards[0] += "┌─────────┐"
        player_cards[1] += "| " + card.image + "      |"
        for count in range(2,4):
            player_cards[count] += "│         │"
        player_cards[4] += "|    " + suites[card.suite] + "    |"
        for count in range(5,7):
            player_cards[count] += "│         │"
        player_cards[7] += "|       " + card.image + "|"
        player_cards[8] += "└─────────┘"

    # CASE 3A: First card needs to be hidden
    if (turn):

        for card in dealer.hand:
                
            # STEP 3AI: Currently first card, need to censor
            if (dealer_first_card):
                dealer_cards[0] += "┌─────────┐"    

                # STEP 3AII: Lines with indexes 1-7 share the same pattern
                for count in range(1,8):
                    dealer_cards[count] += "|░░░░░░░░░|"

                dealer_cards[8] += "└─────────┘"       
                dealer_first_card = False

            # STEP 3AIII: Can openly record remaining cards
            else:
                dealer_cards[0] += "┌─────────┐"
                dealer_cards[1] += "| " + card.image + "      |"
                for count in range(2,4):
                    dealer_cards[count] += "│         │"
                dealer_cards[4] += "|    " + suites[card.suite] + "    |"
                for count in range(5,7):
                    dealer_cards[count] += "│         │"
                dealer_cards[7] += "|       " + card.image + "|"
                dealer_cards[8] += "└─────────┘"

    # CASE 3B: Dealer's turn
    else:
        for card in dealer.hand:
            dealer_cards[0] += "┌─────────┐"
            dealer_cards[1] += "| " + card.image + "      |"
            for count in range(2,4):
                dealer_cards[count] += "│         │"
            dealer_cards[4] += "|    " + suites[card.suite] + "    |"
            for count in range(5,7):
                dealer_cards[count] += "│         │"
            dealer_cards[7] += "|       " + card.image + "|"
            dealer_cards[8] += "└─────────┘"

    # STEP 4: Display the dealer's cards
    print("\n" + BORDER)
    print(f"\n --| DEALER CARDS |--\n")
    if (turn):
        print("Dealer's card sum: ?\n")
    else:
        print(f"Dealer's card sum: {dealer.card_sum}\n")
    for line in dealer_cards:
        print(line)

    # Step 5: Displaying player cards
    print(f"\n --| PLAYER CARDS |--\n\nPlayer's card sum: {player.card_sum}\n")
    for line in player_cards:
        print(line)

# ---------------------------------------------------------------------------- #

def prepare_round(deck, player, dealer, round_number):
        """
        Resets the deck, player & dealer hands, & provides new cards.

        :Parameters:
            - 'deck': an instance of the `Deck` class
            - 'player': an instance of the `Player` class
            - 'dealer': an instance of the `Dealer` class
            - 'round_number': an integer of the current round of black jack

        :Return:
            A boolean where: 
                - `True`: the player already has a black jack
                - `False`: opposite of above (i.e. continue playing the game)
        """

        # STEP 1: Display the round number
        print(f"                                    ROUND: {round_number}\n" + BORDER)

        # STEP 2: Check if deck length is long enough for next round
        if len(Deck.all_cards) <= 26:
                print("\nDECK INSUFFICIENT.")
                Deck.delete_deck()
                Deck.new_deck()
        
        # STEP 3: Reset player & dealer hands
        print("\nResetting player hand...")
        player.reset_hand()
        print("\nResetting dealer hand...")
        dealer.reset_hand()

        # STEP 4: Assign player cards, dealer cards, & update the card sum
        while (len(player.hand) != 2) and (len(dealer.hand) != 2):
                player.add_card(Deck)
                dealer.add_card(Deck)
        print("\nDEALING CARDS...")

        # STEP 5: Check if the player has black jack as their inital hand
        if (player.card_sum == BLACKJACK) and (len(player.hand) == 2):
                return False
        else:
                return True

# ---------------------------------------------------------------------------- #

