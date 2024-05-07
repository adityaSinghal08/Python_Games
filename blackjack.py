# IMPORTS

from IPython.display import clear_output
from random import shuffle
import os



# GLOBAL VARIABLES

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
# By default, the value of Ace is 11 but as per situation, we can use it as 1 within the gameplay.
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}



# CARD CLASS

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit



# DECK CLASS

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def remove_one_card(self):
        if len(self.all_cards) == 0:
            pass
        else:
            return self.all_cards.pop(0)



# CHIPS CLASS

class Chips():

    def __init__(self, amount):
        self.total_amount = amount
    
    def add_chips(self, amount):
        self.total_amount += amount

    def remove_chips(self, amount):
        if amount > self.total_amount:
            pass
        else:
            self.total_amount -= amount



# HAND CLASS

class Hand():

    def __init__(self, amount=0):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.bet_amount = amount
    
    def deal_one_card(self):
        return self.deck.remove_one_card()



# PLAYER CLASS

class Player():

    def __init__(self, name = "Computer", amount = 0):
        self.name = name
        self.deck = []
        self.deck_sum = 0
        self.chips = Chips(amount)

    def __str__(self):
        return f"Player {self.name} holds {len(self.deck)} cards and chips worth of ${self.chips.total_amount}."

    def add_one_card(self, card):
        self.deck.append(card)
        # When card is not an Ace.
        if card.value != 11:
            self.deck_sum += values[card.rank]
        # When card is an Ace.
        else:
            # If using Ace's value as 11 gives a bust, then use value as 1, else use value as 11.
            if self.deck_sum + 11 > 21:
                self.deck_sum += 1
            else:
                self.deck_sum += 11
    
    def bet_chips(self, amount):
        self.chips.remove_chips(amount)



# ASKING THE PLAYER FOR CHIPS AMOUNT - FUNCTION

def ask_player_chips_amount():

    player_chips_amount = "WRONG"

    # Validifying the chips amount (>0)
    while player_chips_amount.isdigit() == False:

        player_chips_amount = input("Enter your chips amount: ")

        # Print an error message for the player.
        if player_chips_amount.isdigit() == False or int(player_chips_amount) < 0:
            os.system('cls')
            print("You haven't entered a whole amount.")
            print("Please try again!\n")
        elif int(player_chips_amount) == 0:
            os.system('cls')
            print("You must have some chips to bet.")
            print("Please try again!\n")

    return int(player_chips_amount)



# ASKING THE PLAYER FOR BETTING AMOUNT - FUNCTION

def ask_player_betting_amount(human_player):
    betting_amount = "WRONG"
    betting_amount_in_range = False
    # Validifying the betting amount
    while betting_amount.isdigit() == False or betting_amount_in_range == False:

        betting_amount = input("Enter your bet amount: ")

        # Print an error message for the player.
        if betting_amount.isdigit() == False or int(betting_amount) < 0:
            os.system('cls')
            print("You haven't entered a whole amount.")
            print("Please try again!\n")
        elif int(betting_amount) == 0:
            os.system('cls')
            print("You must bet some chips.")
            print("Please try again!\n")
        elif int(betting_amount) > human_player.chips.total_amount:
            os.system('cls')
            print("Your betting amount exceeds your available chips amount.")
            print(f"Available chips amount: {human_player.chips.total_amount}")
            print("Please try again!\n")
        else:
            # Betting amount is an affordable whole amount
            betting_amount_in_range = True

    return int(betting_amount)



# ASKING PLAYER HITTING CHOICE - FUNCTION

def ask_player_hit_choice(automated_player, human_player):
    player_choice = "WRONG"

    # Validifying player choice
    while player_choice not in ('Y', 'N'):

        player_choice = input("\nDo you want to hit (Y/N): ")
        player_choice = player_choice.upper()

        # Printing error message for the player.
        if player_choice not in ('Y', 'N'):
            os.system('cls')
            display_cards(automated_player, human_player, False)
            print("\nYou haven't entered a valid choice.")
            print("Please try again!\n")

    return player_choice == 'Y'



# ASKING PLAYER FOR CONTINUING GAME - FUNCTION

def ask_player_game_on_choice():
    player_choice = "WRONG"

    # Validifying player choice
    while player_choice not in ('Y', 'N'):

        player_choice = input("\nDo you want to continue playing (Y/N): ")
        player_choice = player_choice.upper()

        # Printing error message for the player.
        if player_choice not in ('Y', 'N'):
            os.system('cls')
            print("You haven't entered a valid choice.")
            print("Please try again!\n")

    return player_choice == 'Y'



# DISPLAYING THE CARDS

# The visible argument determines whether all of computer cards are visible or only first
def display_cards(automated_player, human_player, visible):
    
    os.system('cls')

    automated_cards = "{0:^19}".format(automated_player.deck[0].__str__())

    for i in range(1,len(automated_player.deck)):
        if visible == True:
            automated_cards += "|" + "{0:^19}".format(automated_player.deck[i].__str__())
        else :
            automated_cards += "|" + "{0:^19}".format("*****")

    human_cards = "{0:^19}".format(human_player.deck[0].__str__())

    for i in range(1,len(human_player.deck)):
        human_cards += "|" + "{0:^19}".format(human_player.deck[i].__str__())
    
    print("-" * len("| AUTOMATED PLAYER CARDS |"))
    print("| AUTOMATED PLAYER CARDS |")
    print("-" * len("| AUTOMATED PLAYER CARDS |") + "\n")

    print(automated_cards + "\n")

    print("-" * len(f"| PLAYER {human_player.name.upper()}'S CARDS |"))
    print(f"| PLAYER {human_player.name.upper()}'S CARDS |")
    print("-" * len(f"| PLAYER {human_player.name.upper()}'S CARDS |") + "\n")

    print(human_cards + "\n")
    


# RESET THE PLAYER'S CARDS

def reset_players(automated_player, human_player):
    automated_player.deck = []
    automated_player.deck_sum = 0
    human_player.deck = []
    human_player.deck_sum = 0



# GAMEPLAY FUNCTION

def start_game():

    os.system('cls')

    # AUTOMATED PLAYER
    automated_player = Player()

    # HUMAN PLAYER
    player_name = input("Enter your name: ")
    os.system('cls')

    player_chips_amount = ask_player_chips_amount()

    human_player = Player(player_name, player_chips_amount)

    # GAMEPLAY VARIABLES
    game_on = True

    # LET'S PLAY
    while game_on:

        os.system('cls')

        #Resetting the players cards at start of each game
        reset_players(automated_player, human_player)

        # DISPLAY USER INFO AT START OF EACH GAME
        print(f"Player Name: {human_player.name}")
        print(f"Player Chips: {human_player.chips.total_amount}\n")

        # THE DEALING HAND
        betting_amount = ask_player_betting_amount(human_player)
       
        # Betting the chips
        human_player.bet_chips(betting_amount)

        dealer = Hand(betting_amount)

        # DEALING TWO CARDS TO THE HUMAN AND AUTOMATED PLAYERS AT BEGINNING OF THE GAME
        automated_player.add_one_card(dealer.deal_one_card())   # The automated players's only visible card
        automated_player.add_one_card(dealer.deal_one_card())

        human_player.add_one_card(dealer.deal_one_card())
        human_player.add_one_card(dealer.deal_one_card())

        bust = False
        hit = True

        #
        # Whenever I refer to player, I mean the human player.
        #

        # ASKING THE PLAYER TO HIT OR STAY
        while bust == False and hit == True:

            display_cards(automated_player, human_player, False)

            hit = ask_player_hit_choice(automated_player, human_player)

            # Hit a card if player wishes
            if hit == True:

                human_player.add_one_card(dealer.deal_one_card())

                # If sum of deck is greater than 21, player is busted.
                bust = (human_player.deck_sum > 21)

        # IN CASE THE PLAYER GOT BUSTED, PRINT LOSING MESSAGE FOR PLAYER.
        if bust == True:

            display_cards(automated_player, human_player, True)

            print(f"\n\nPlayer {human_player.name} got BUSTED.")
            print(f"Player {human_player.name} LOST the game.")
            print("GOOD LUCK next time!\n\n")
        
        # IF PLAYER NOT BUSTED, IT'S COMPUTER'S TURN.
        else:
            bust = False
            hit = (automated_player.deck_sum < 17 ) # Computer keeps hitting if deck sum is less than 17

            while bust == False and hit == True:

                automated_player.add_one_card(dealer.deal_one_card())

                # Check if computer is busted.
                bust = (automated_player.deck_sum > 21)
                # Check is hit is possible.
                hit = (automated_player.deck_sum < 17 )
        
            # IF COMPUTER BUSTED, PRINT WINNING MESSAGE FOR PLAYER.
            if bust == True:

                display_cards(automated_player, human_player, True)

                print(f"\n\nAutomated Player got BUSTED.")
                print(f"Player {human_player.name} WON the game.")
                print("SEE YOU AGAIN!\n\n")
                # Add 2 times the betted amount to player's chips
                human_player.chips.add_chips(2 * dealer.bet_amount)

             # IN CASE PLAYER AS WELL AS COMPUTER NOT BUSTED, CHECK THE WINNER MANUALLY.
            else:
                # Whoever is close to 21 is the winner. If both equal, declare player as winner.
                if human_player.deck_sum >= automated_player.deck_sum:

                    display_cards(automated_player, human_player, True)

                    print(f"\n\nPlayer {human_player.name} is closer to 21.")
                    print(f"Player {human_player.name} WON the game.")
                    print("SEE YOU AGAIN!\n\n")
                    human_player.chips.add_chips(2 * dealer.bet_amount)
                else:

                    display_cards(automated_player, human_player, True)

                    print("\n\nAutomated Player is close to 21.")
                    print(f"Player {human_player.name} LOST the game.")
                    print("GOOD LUCK next time!\n\n")

        game_on = ask_player_game_on_choice()



# LET'S START THE GAME

start_game()

