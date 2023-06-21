import os

def clear_output():
    os.system('clear')


# Tic Tac Toe Game
def display_board():
    row_1 = board_dict[1] + " | " + board_dict[2] + " | " + board_dict[3]
    row_2 = board_dict[4] + " | " + board_dict[5] + " | " + board_dict[6]
    row_3 = board_dict[7] + " | " + board_dict[8] + " | " + board_dict[9]
    div_1 = "-" + "---" + "-" + "---" + "-"
    print(row_1)
    print(div_1)
    print(row_2)
    print(div_1)
    print(row_3)
    print("\n")


# Display number board to take input
def display_num_board():
    row_1 = "1" + " | " + "2" + " | " + "3"
    row_2 = "4" + " | " + "5" + " | " + "6"
    row_3 = "7" + " | " + "8" + " | " + "9"
    div_1 = "-" + "---" + "-" + "---" + "-"
    print(row_1)
    print(div_1)
    print(row_2)
    print(div_1)
    print(row_3)
    print("\n")


# Input players name
# players = {"player1" : {"name" : "player1", "symbol": "X"}, "player2": {"name" : "player1", "symbol": "O"}}
def get_players_name():
    players['player1']['name'] = input("Player 1 enter your name : \n")

    # To check correct symbol
    keep_symbol_check = True
    while keep_symbol_check:
        symbol_input = input(
            f"{players['player1']['name']} choose your symbol X or O: \n")
        if symbol_input.upper() in ["X", "O"]:
            players['player1']['symbol'] = symbol_input.upper()
            keep_symbol_check = False
        else:
            print("Please either X or O")

    players['player2']['name'] = input("Player 2 enter your name : \n")

    # Assign symbol to other player
    if players['player1']['symbol'] == "X":
        players['player2']['symbol'] = "O"
    else:
        players['player2']['symbol'] = "X"

    # Display players info
    print(
        f"Player1 : {players['player1']['name']} your symbol : {players['player1']['symbol']}")
    print(
        f"Player2 : {players['player2']['name']} your symbol : {players['player2']['symbol']}")


def user_choice():
    input_check = False
    while not input_check:

        # To get current turn player name
        if turn % 2 == 0:
            player_name = players['player1']['name']
        else:
            player_name = players['player2']['name']

        position_input = input(f" {player_name} Please enter a position : ")
        if not position_input.isdigit():
            print("Not a valid number")
        elif int(position_input) not in range(1, 10):
            print("Number not in the range (1,9)")
        elif board_dict[int(position_input)] == "X" or board_dict[int(position_input)] == "O":
            print("This position is already marked")
        else:
            input_check = True

    return int(position_input)


# to mark the position
# player1_moves = []
# player2_moves = []
def mark_position(board_dict, position_input, turn):
    # player 1
    if turn % 2 == 0:
        board_dict[position_input] = players['player1']["symbol"]
        player1_moves.append(position_input)
    else:
        board_dict[position_input] = players['player2']["symbol"]
        player2_moves.append(position_input)


# get combinations
# A Python program to print all
# combinations of given length
def get_combinaions(player_moves_list):
    from itertools import combinations

    # combinations(list, length)
    comb = combinations(player_moves_list, 3)
    return list(comb)


# get_winner
def get_winner():
    if turn >= 4:
        player1_combinations_list = get_combinaions(player1_moves)
        player2_combinations_list = get_combinaions(player2_moves)
#         print(player1_combinations_list)
#         print(player2_combinations_list)
        for win_set in winning_list:
            for com1_set in player1_combinations_list:
                if (win_set == set(com1_set)):
                    return "player1"
            for com2_set in player2_combinations_list:
                if (win_set == set(com2_set)):
                    return "player2"


def gameon_choice():
    gameon_check = False
    while not gameon_check:
        gameon_input = input("Do you want to play again? 'y' or 'n' : ")
        if gameon_input.lower() not in ['y', 'n']:
            print("Not a valid choice")
        else:
            return gameon_input.lower() == 'y'


##################### Game ##########################
gameon = True
while gameon:
    print("################################### Welcome to the game! #####################################")
    board_dict = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }
    players = {"player1": {"name": "player1", "symbol": "X"},
               "player2": {"name": "player1", "symbol": "O"}}
    winning_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {
        1, 5, 9}, {7, 5, 3}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}]
    turn = 0
    get_players_name()
    player1_moves = []
    player2_moves = []
    while turn < 9:
        clear_output()  # Only for jupyter notebook
        display_num_board()
        display_board()
        position_input = user_choice()
        mark_position(board_dict, position_input, turn)
        if get_winner():
            clear_output()  # Only for jupyter notebook
            display_num_board()
            display_board()
            print("\n ########################### ^^^^^ ######################## \n")
            print(f"Congratulation {players[get_winner()]['name']}, you won!")
            break
        turn += 1
    #     print(player1_moves)
    #     print(player2_moves)
    else:
        print("Match Drawn!")

    gameon = gameon_choice()
