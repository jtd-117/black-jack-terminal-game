# @file	    main.py
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

# LIBRARIES:
import black_jack as bj

# ---------------------------------------------------------------------------- #

# MAIN FUNCTION:
if __name__ == "__main__":
        
    print("\n" + bj.BORDER)
    print("                            PYTHON PROGRAM - BLACK JACK")
    print("                                Jude Thaddeau Data")
    print(bj.BORDER)

    # STEP 1: Initialise game meta-data, players & automated dealer
    play_black_jack = True
    round_count = 0
    deck = bj.Deck()
    player = bj.Players()
    dealer = bj.Dealers()

    # STEP 2: Provide a mechanism for replayability of multiple rounds
    while (play_black_jack):

        # STEP 3: Initialise the variables for the current round
        round_count += 1
        player_turn = None
        player_insurance = None
        bj.deal_round(player)
        player_turn = bj.prepare_round(deck, player, dealer, player_turn, round_count)
        bj.display_table(player,dealer, player_turn)

        # STEP 4: If possible, check if the player wants INSURANCE
        player_insurance = bj.insurance(player, dealer)

        # STEP 5: If possible, check if the player wants to DOUBLE-DOWN
        player_turn = bj.double_down(deck, player, dealer, player_turn)

        # STEP 6: It is the PLAYER's turn to hit or stand
        while (player_turn):

            # STEP 6A: Allow player input & display board
            player_turn = bj.player_turns(deck, player)
            bj.display_table(player, dealer, player_turn)

        # STEP 7: Check if the player BUSTED
        if (player.card_sum > bj.BLACKJACK):
            print(bj.BORDER + "\n                                     OUTCOME")
            print(bj.BORDER + "\n\nPLAYER BUST!")
            print(f"\nYOU LOSE!\n\nYou lost ${player.bet} to the house.")
            play_black_jack = bj.new_round(player)

            # CASE 7A: The player has enough funds to continue
            if (play_black_jack):
                    continue
                    
            # CASE 7B: The player DOES not have enough funds to continue
            else:
                    break

        # STEP 8: It is the DEALER'S turn to hit or stand
        while (not player_turn):

            # STEP 8A: Automate dealer decisions & display board
            player_turn = bj.dealer_turns(deck, dealer)
            bj.display_table(player, dealer, player_turn)

            # STEP 8B: Check if player decided to stay or ended up busting
            if (player_turn == None):
                    break
        
        # STEP 9: Need to check if dealer busted
        if (dealer.card_sum > bj.BLACKJACK):

            # STEP 9A: Give equal pay to the player
            print(bj.BORDER + "\n                                     OUTCOME")
            print(bj.BORDER + "\n\nDEALER BUST!")
            player.bet *= 3
            player.bank += player.bet
            print(f"\nYOU WIN!\n\n${player.bet} was added to your balance")

        # STEP 10: Check if the player or dealer won given no bust
        if ((player.card_sum <= bj.BLACKJACK) and (dealer.card_sum <= bj.BLACKJACK)):
            bj.board_analysis(player, dealer, player_insurance)

        # STEP 11: Check if the player wants to play again
        play_black_jack = bj.new_round(player)

    # STEP 12: Player lost ALL funds or does not want to play anymore
    print("\nPROGRAM COMPLETE...\n")
    print(bj.BORDER + "\n")