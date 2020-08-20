row1 = ['   ', "|", '   ', '|', '   ', '\n''   ', "|", '   ', '|', '   ', '\n', '___', "|", '___', '|', '___']
row2 = ['   ', '   ', '   ', '\n''   ', "|", '   ', '|', '   ', '\n', '   ', '|', '   ', '|', '   ''\n', '___', "|",
        '___', '|', '___']
row3 = ['   ', '   ', '   ', '\n''   ', "|", '   ', '|', '   ', '\n', '   ', '|', '   ', '|', '\n', '   ', '|', '   ',
        '|', '   ']
player1 = ""
player2 = ""
player1_dict = {'symbol': '', 'victories': '', 'moves': []}
player2_dict = {'symbol': '', 'victories': '', 'moves': []}
currently_moving_X = True
currently_moving_symbol = ""
game_on = False


def display(row1, row2, row3):
    for item in row1:
        print(item, end="")
    for item in row2:
        print(item, end="")
    for item in row3:
        print(item, end="")
    print()


def user_initial_input():
    global player1
    global player2
    player1 = input("Please enter name of player 1: ")
    print("Hello " + player1)
    player2 = input("Please enter name of player 2: ")
    print("Hello " + player2)
    return player1, player2


def user_history(player1_dict, player2_dict):
    q1 = input(f"Would {player1} like to play as 'x'? 'Y' or 'N' ")
    q1 = q1.lower()
    if q1 != "y" and q1 != "n":
        while q1 != "y" and q1 != "n":
            q1 = input().lower()
            print(f"I am not sure I understand. Let's try again. Would {player1} like to play as 'x'? Please answer with 'Y' for 'yes' and 'N' for 'No'.")
        if q1 == 'y':
            player1_dict['symbol'] = "X"
            player2_dict['symbol'] = "O"
        elif q1 == 'n':
            player1_dict['symbol'] = "O"
            player2_dict['symbol'] = "X"


def move(currently_moving_symbol):

    #function that will alternate variables on the board after accepting user input and changes

    move = input("Enter a number 1 - 9: ")

    while move.isdigit() == False or int(move) > 9 or int(move) < 1 or move in player1_dict['moves'] or move in player2_dict['moves']:
        print("That won't work, lets try again!")
        move = input("Enter a number 1 - 9: ")

    move = int(move)
    global currently_moving_X
    currently_mocing_X = False
    if move < 4:
        global row1

        if move == 1:
            row1[6] = currently_moving_symbol
        elif move == 2:
            row1[8] = ' ' + currently_moving_symbol + ' '
        elif move == 3:
            row1[10] = ' ' + currently_moving_symbol + ' '

    elif move > 3 and move < 7:
        global row2

        if move == 4:
            row1[0][1] = currently_moving_symbol
        elif move == 5:
            row1[0][1] = currently_moving_symbol
        elif move == 6:
            row1[0][1] = currently_moving_symbol

    elif move > 6:
        global row3

        if move == 7:
            row1[0][1] = currently_moving_symbol
        elif move == 8:
            row1[0][1] = currently_moving_symbol
        elif move == 9:
            row1[0][1] = currently_moving_symbol


def announce_move():
    global currently_moving_symbol
    if player1_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player1}!")
        currently_moving_symbol = 'X'
    elif player1_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player2}!")
        currently_moving_symbol = 'O'
    elif player2_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player2}!")
        currently_moving_symbol = 'X'
    elif player2_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player1}!")
        currently_moving_symbol = 'O'


user_initial_input()
user_history(player1_dict, player2_dict)
display(row1, row2, row3)
announce_move()
move(currently_moving_symbol)
display(row1, row2, row3)
move(currently_moving_symbol)
display(row1, row2, row3)