# IMPORT LIBRARIES

from IPython.display import clear_output
from random import randint
import os


#--------------------------------------------------------------------------------------



# DISPLAY BOARD

def display_board(board_list):

    print("\n     |     |     ")
    print(f'  {board_list[0]}  |  {board_list[1]}  |  {board_list[2]}  ')
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f'  {board_list[3]}  |  {board_list[4]}  |  {board_list[5]}  ')
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f'  {board_list[6]}  |  {board_list[7]}  |  {board_list[8]}  ')   
    print("     |     |     \n")

# CHECK
# board_list = [1,2,' ',4,5,6,7,8,9]
# display_board(board_list)



#--------------------------------------------------------------------------------------



# DETERMINE WHICH PLAYER'S TURN IT IS

def check_player_turn(current_player):

    # when the game just startes, chose a player to start at random
    if current_player == 0:
        return randint(1, 2)
    # when the previous move was played by player-1
    elif current_player == 1:
        return 2
    # when the previous move was played by player-2
    else:
        return 1
    
# CHECK
# current_player = 0
# current_player = check_player_turn(current_player)
# print(current_player)



#--------------------------------------------------------------------------------------



# ASK PLAYER FOR A POSITION INDEX TO PLACE THEIR SYMBOL

def ask_symbol_position(board_list, current_player):

    choice = "wrong"    
    acceptable_range = range(1,10)
    choice_in_range = False # tracks if choice is in acceptable range
    choice_position_empty = False # tracks if chosen position is empty

    # prompt the player to make sure they know it is their turn
    if current_player == 1:
        print("Player 1's Turn\n")

    else:
        print("Player 2's Turn\n")

    # loop keeps running until user makes a valid choice
    while choice.isdigit() == False or choice_in_range == False or choice_position_empty == False:
        
        # makes sure all variables are false before the user makes another choice
        choice_in_range = False
        choice_position_empty = False

        choice = input("Please enter a board index between 1 to 9: ")

        # when choice is not a digit
        if choice.isdigit() == False:

            clear_output()
            print("You have not entered an integer. Try again!\n")

        # when choice is a digit
        else:

            # when choice is not within 1 to 9
            if int(choice) not in acceptable_range:

                clear_output()
                print("You have not entered a number between 1 to 9. Try again!\n")

            # when choice is a digit within 1 to 9
            else:

                choice_in_range = True

                # when chosen position is not empty
                if board_list[int(choice)-1] != ' ':

                    clear_output()
                    print("The position you entered is occupied. Please enter an empty index.\n")
                
                # when choice is a digit between 1 to 9 and the corresponding position is empty
                # this case will make all the requirements true and we will break out of the loop
                else:

                    choice_position_empty = True
    
    # return a validated choice
    return int(choice)

# CHECK
# ask_symbol_position(board_list)



#--------------------------------------------------------------------------------------



# PLACE THE PLAYER'S SYMBOL AT CHOSEN POSITION

def place_symbol(board_list, current_player, symbol_position):
    
    # player-1's symbol is 'X'
    if current_player == 1:
        board_list[symbol_position - 1] = 'X'
    # player-2's symbol is 'O'
    else:
        board_list[symbol_position - 1] = 'O'

# CHECK
# board_list = ['', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O']
# current_player = 2
# symbol_position = 1
# place_symbol(board_list, current_player, symbol_position)
# display_board(board_list)



#--------------------------------------------------------------------------------------



# CHECK THE GAME STATUS

def check_game_status(board_list):

    # given are the four possible game status:
        # T for Tied
        # C for Continue (Still on)
        # W1 for Player 1 Won
        # W2 for Player 2 Won

    # find out if the board is full
    board_full = True

    for position in board_list:

        if position == ' ':
            board_full = False
            break
     
    # check for the upper row pattern   
    if board_list[0] != ' ' and board_list[0] == board_list[1] == board_list[2]:

        if board_list[0] == 'X':
            return "W1"
        else:
            return "W2"
        
    # check for the middle row pattern
    if board_list[3] != ' ' and board_list[3] == board_list[4] == board_list[5]:

        if board_list[3] == 'X':
            return "W1"
        else:
            return "W2"

    # check for the bottom row pattern 
    if board_list[6] != ' ' and board_list[6] == board_list[7] == board_list[8]:

        if board_list[6] == 'X':
            return "W1"
        else:
            return "W2"
        
    # check for the left column pattern
    if board_list[0] != ' ' and board_list[0] == board_list[3] == board_list[6]:

        if board_list[0] == 'X':
            return "W1"
        else:
            return "W2"
        
    # check for the middle column pattern
    if board_list[1] != ' ' and board_list[1] == board_list[4] == board_list[7]:

        if board_list[1] == 'X':
            return "W1"
        else:
            return "W2"
        
    # check for the right column pattern    
    if board_list[2] != ' ' and board_list[2] == board_list[5] == board_list[8]:

        if board_list[2] == 'X':
            return "W1"
        else:
            return "W2"
        
    # ckeck for the upper-left to lower-right diagonal pattern
    if board_list[0] != ' ' and board_list[0] == board_list[4] == board_list[8]:

        if board_list[0] == 'X':
            return "W1"
        else:
            return "W2"
        
    # check for the upper-right to lower-left diagonal pattern
    if board_list[2] != ' ' and board_list[2] == board_list[4] == board_list[6]:

        if board_list[2] == 'X':
            return "W1"
        else:
            return "W2"
        
    # if the board is full and no one won the game, return tied
    if board_full == True:
        return 'T'
    # when some positions are still empty and no one won the game, return continue
    else:
        return 'C'
    
# CHECK
# board_list = ['X', 'X', 'O', 'O', 'O', 'X', 'O', 'X', 'O']
# status = check_game_status(board_list)
# print(status)



#--------------------------------------------------------------------------------------



# ASK IF THE PLAYERS WANT TO KEEP PLAYING

def ask_player_intention():

    choice = 'wrong'

    # until user enters a valid choice, keep asking
    while choice not in ['y', 'n', 'Y', 'N']:

        choice = input("Do you want to keep playing? Enter Y/N: ")

        # if the choice is not Y/N or y/n
        if choice not in ['y', 'n', 'Y', 'N']:

            clear_output()
            print("I don't understand. Please enter your choice again.\n")
    
    return choice.capitalize()

# CHECK
# game_on = ask_player_intention()
# print(game_on)


#--------------------------------------------------------------------------------------



# PRINT THE FINAL RESULT OF THE GAME

def print_result(board_list, game_status):

    os.system('cls')

    print('\n***********************************************************************')
    print('                                  GAME ENDED                               ')
    print('***********************************************************************')

    # display the final board
    display_board(board_list)

    if game_status == 'T':
        print("The game is TIED between Player 1 and Player 2.\n")

    elif game_status == 'W1':
        print("The game is WON by Player 1.\n")

    else:
        print("The game is WON by Player 2.\n")
    



#--------------------------------------------------------------------------------------



# RESET THE BOARD FOR A NEW GAME

def reset_game(board_list, current_player, game_status):

    for i in range(9):
        board_list[i] = ' '
    
    current_player = 0

    game_status = 'C'



#--------------------------------------------------------------------------------------
#                                                                                     #
#                    T H E    T I C - T A C - T O E   G A M E                         #
#                                                                                     #
#--------------------------------------------------------------------------------------



def start_game():

    # VARIABLES
    board_list = [1,2,3,4,5,6,7,8,9]
    current_player = 0
    game_status = ''
    game_on = True
    
    # RESET THE BOARD FOR A NEW GAME
    reset_game(board_list, current_player, game_status)

    # KEEP RUNNING WHILE THE GAME IS ON
    while game_on == True:

        #Clear the terminal at each player's turn
        os.system('cls')

        # DISPLAY THE BOARD
        display_board(board_list)

        # UPDATE THE CURRENT PLAYER
        current_player = check_player_turn(current_player)

        # ASK FOR THE SYMBOL POSITION
        symbol_position = ask_symbol_position(board_list, current_player)

        # PLACE THE SYMBOL ON THE BOARD
        place_symbol(board_list, current_player, symbol_position)

        # CHECK THE GAME STATUS
        game_status = check_game_status(board_list)

        # IF THE GAME IS AT CONCLUSION
        if game_status in ['T', 'W1', 'W2']:
            
            print_result(board_list, game_status)

            # ASK USER IF THEY WANT TO KEEP PLAYING
            game_on = (ask_player_intention() == 'Y')

            # RESET THE GAME IF USERS WANT TO START A NEW GAME
            if game_on == True:
                reset_game(board_list, current_player, game_status)
            else:
                os.system('cls')
                print('\nThank you for playing! See you soon...\n')


# LET'S PLAY THE GAME
start_game()