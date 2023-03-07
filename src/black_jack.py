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
    
    def add_card(self, deck):
        """
        Adds a card to the player's hands.
        """
        
        # STEP 1: Need to add card to hand AND remove same card from deck
        self.hand.append(deck.all_cards[0])
        deck.all_cards.pop(0)
        
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
    if len(deck.all_cards) <= 26:
        print("\nDECK INSUFFICIENT.")
        deck.delete_deck()
        deck.new_deck()
    
    # STEP 3: Reset player & dealer hands
    print("\nResetting player hand...")
    player.reset_hand()
    print("\nResetting dealer hand...")
    dealer.reset_hand()

    # STEP 4: Assign player cards, dealer cards, & update the card sum
    while (len(player.hand) != 2) and (len(dealer.hand) != 2):
        player.add_card(deck)
        dealer.add_card(deck)
    print("\nDEALING CARDS...")

    # STEP 5: Check if the player has black jack as their inital hand
    if (player.card_sum == BLACKJACK) and (len(player.hand) == 2):
        return False
    else:
        return True

# ---------------------------------------------------------------------------- #

def insurance(player, dealer):
    """
    Allows the player to place half of their intial bet as insurance 
    against a potential black jack hand belonging to the dealer.

    :Parameters:
        - 'player': an instance of the `Player` class
        - 'dealer': an instance of the `Dealer` class

    :Return:
        A boolean value where:
            - `True`: indicates the transaction was ACCEPTED
            - `False`: indicates the transaction was DECLINED
    """

    # STEP 1: Calculate player insurance amount
    player.insurance = player.bet/2

    # CASE 2A: Second card is NOT an 'Ace'
    if (dealer.hand[-1].rank != 'Ace'):
        return False

    # CASE 2B: Player has black jack in inital hand (WORST CASE: PUSH)
    elif (player.card_sum == BLACKJACK) and (len(player.hand) == 2):
        return False

    # CASE 2C: Player has insufficient funds to pay for insurance
    elif (player.bank - player.insurance < BROKE):
        return True
    
    # STEP 3: Offer insurance
    print(BORDER)
    print("                                OFFER - INSURANCE\n" + BORDER)
    print(f"\n--| Current balance: ${player.bank} |--")
    print(f"\nExtra 'insurance' cost: ${player.insurance}")
    while True:
        try:    
            decision = input("\nWould you like to pay insurance? y)es or n)o: ")
        except:
            print(INVALID)
            continue
        else:   
            # CASE 3A: Player provides inappropriate response
            if decision not in yes_no:
                print(INVALID)
                continue

            # CASE 3B: Player declines insurance offer
            elif decision == yes_no[1]:
                print("\nTRANSACTION DECLINED...\n")
                return False

            # CASE 3C: Player input is accepted
            else:   
                print("\nTRANSACTION ACCEPTED...\n")
                break
    
    # STEP 4: Accept insurance transaction
    player.bank -= player.insurance
    return True

# ---------------------------------------------------------------------------- #

def double_down(deck, player, dealer, turn):
    """
    Allows players to double inital bet after seeing inital cards.

    :Parameters:
        - 'deck': an instance of the `Deck` class
        - 'player': an instance of the `Player` class
        - 'dealer': an instance of the `Dealer` class
        - 'turn': a boolean where 'True' represents Player turn & 'False' for the dealer

    :Return:
        A boolean value where:
            - `True`: indicates the transaction was ACCEPTED
            - `False`: indicates the transaction was DECLINED
    """

    # CASE 1A: Player has blackjack in initial hand (double-down redundant)
    if (player.card_sum == BLACKJACK) and (len(player.hand) == 2):
        return False

    # CASE 1B: Player has insufficient funds to double down
    elif (player.bank - player.bet < BROKE):
        return True
    
    # STEP 2: Ensure player input is correct
    print(BORDER)
    print("                              OFFER - DOUBLE DOWN\n" + BORDER)
    print(f"\n--| Current balance: ${player.bank} |--")
    print(f"\nExtra 'double-down' cost: ${player.bet}.")
    print("\nWould you like to 'double-down' on your bet?")

    # STEP 3: Accept player input
    while True:
        try:    
            decision = input("\ny)es or n)o: ")
        except:
            print(INVALID)
            continue
        else:   

            # CASE 2A: player gives invalid input
            if decision.lower() not in yes_no:
                print(INVALID)
                continue

            # CASE 2B: Player says no
            elif decision.lower() == yes_no[1]:
                print("\nTRANSACTION DECLINED...\n")
                return True
                    
            # CASE 2C: Player says yes
            else:
                print("\nTRANSACTION ACCEPTED...")
                break
    
    # STEP 3: Supply another card & display board
    print("\nProviding player with another card...")
    player.add_card(deck)
    player.bank -= player.bet
    player.bet *= 2
    display_table(player, dealer, turn)
    return False

# ---------------------------------------------------------------------------- #

def player_turn(deck, player):
    """
    Allows the player to hit or stand & calculates if the player busts

    :Parameters:
        - 'player': an instance of the `Player` class

    :Return:
        A boolean where:
            - `True`: it is still the player's turn
            - `False`: it is the dealer's turn
    """

    # STEP 1: Check if the player wants to HIT or STAND
    print(BORDER + "\n                                   PLAYER TURN\n" + BORDER)
    while True:
        try:      
            decision = input("\nWould you like to h)it or s)tand: ")

        except:
            print(INVALID)
            continue

        else:   

            # CASE 1A: Player provides inappropriate response
            if decision.lower() not in stand_hit:
                print(INVALID)
                continue

            # CASE 1B: Player decides to stand
            elif decision.lower() == stand_hit[0]:
                return False
            
            # CASE 1C: Player decides to hit
            else:   
                break

    # STEP 2: Assign random card
    player.add_card(deck)

    # STEP 3: Check if player busts
    if player.card_sum >= BLACKJACK:
            return False
    
    # STEP 4: Indicate it is still the player's turn
    return True

# ---------------------------------------------------------------------------- #

def dealer_turn(deck, dealer):
    """
    Automates dealer's hit or stand tactics.

    :Parameters:
        - 'deck': an instance of the `Deck` class
        - 'dealer': an instance of the `Dealer` class
    """

    # STEP 1: Indicate it is the dealers turn
    print(BORDER + "\n                                 DEALER TURN\n" + BORDER)

    # CASE 2A: Dealer Stands
    if (RISKYBOUNDARY <= dealer.card_sum <= BLACKJACK):
        print("\nDealer decision: STAND")
        return None
    
    # CASE 2B: Dealer Hits
    else:
        print("\nDealer decision: HIT")
        dealer.add_card(deck)
    
    # STEP 3: Check if dealers busts
    if dealer.card_sum > BLACKJACK:
        return None
    
    # STEP 4: Indicate it is still the dealer's turn
    return False

# ---------------------------------------------------------------------------- #

def board_analysis(player, dealer, insurance):
    """
    Checks whether the player or dealer won or drawed.

    :Parameters:
        - 'player': an instance of the `Player` class
        - 'dealer': an instance of the `Dealer` class
        - 'insurance': a boolean of whether insurance was payed for
    """

    # STEP 1: Indicate that the round has concluded
    print(BORDER + "\n                                     OUTCOME")
    print(BORDER + "\n")

    # CASE 2A: Draw
    if (player.card_sum == dealer.card_sum):

        # STEP 2AI: Return EQUAL money
        print(f"PUSH!\n\n${player.bet} was returned to your account balance.")
        player.bank += player.bet
    
    # CASE 2B: Player wins
    elif (player.card_sum > dealer.card_sum):

        # STEP 2BI: Return 2X money
        player.bet *= 2
        player.bank += player.bet
        print(f"YOU WIN!\n\n${player.bet} was added to your balance.")

    # CASE 2C: Dealer wins via black jack given insurance
    elif (len(dealer.hand) == 2) and (dealer.card_sum == BLACKJACK) and insurance:

        # STEP 2CI: Substitute inital bet with the insurance payment
        player.bank += player.bet
        print(f"YOU LOSE!\n\nYou lost ${player.insurance} to the house.")

    # CASE 4: Dealer wins
    else:
        print(f"YOU LOSE!\n\nYou lost ${player.bet} to the house.")

# ---------------------------------------------------------------------------- #

def new_round(player):
    """
    Allows player to decide is they want to play again.

    :Parameters:
        - `player`: an instance of the `Player` class

    :Return:
        A boolean where:
            - `True`: The player wants to play again
            - `False`: The player does NOT want to play again
    """

    # CASE 1A: Player has no more money (i.e. gamer over - terminate program)
    print("\n" + BORDER)
    if player.bank <= BROKE:
        print("\nNO FUNDS AVAILIABLE. GET OUT OF THIS CASINO!")
        return False

    # CASE 1B: Player gets to decide to play again
    print("                                 REPLAY REQUEST\n" + BORDER)
    print("\nFUNDS SUFFICIENT...")

    while True:
        try:    
            decision = input("\nWould you like to play again? y)es or n)o: ")

        except:
            print(INVALID)
            continue

        else:
            # CASE 1BI: Player provides inappropriate response
            if decision.lower() not in yes_no:
                print(INVALID)
                continue

            # CASE 1BII: Player decides to play another round
            elif decision.lower() == yes_no[0]:
                print("\nEXCELLENT... YOUR MONEY BELONGS TO THE CASINO!")
                print("\n" + BORDER)
                return True

            # CASE 1BIII: Player decides to terminate program
            else:   
                print("\nCOME BACK SOON. THE CASINO NEEDS YOUR MONEY!")
                return False