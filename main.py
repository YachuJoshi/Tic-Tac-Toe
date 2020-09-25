from random import randint


def print_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]} ")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]} ")
    print("---------")
    print(f"{board[1]} | {board[2]} | {board[3]} ")


def user_choice():
    choice = "wrong"
    within_range = False

    while choice.isdigit() == False or within_range == False:

        choice = input("Enter a number from (1-9): ")

        if choice.isdigit():
            if int(choice) in range(1, 10):
                within_range = True
            else:
                within_range = False
                print("Sorry, that number is out of bound")
        else:
            print("Sorry, that is not a number")

    return int(choice)


def check_win_condition(board):
    win_condition_one = ["X", "X", "X"]
    win_condition_two = ["O", "O", "O"]

    # Row win condition

    for i in range(1, 10, 3):
        if board[i : i + 3] == win_condition_one or (
            board[i : i + 3] == win_condition_two
        ):
            return True

    # Column win condition

    for i in range(1, 4):
        if (board[i:10:3] == win_condition_one) or (board[i:10:3] == win_condition_two):
            return True

    # Diagonal win condition

    if board[1:10:4] == win_condition_one or board[1:10:4] == win_condition_two:
        return True
    if board[3:9:2] == win_condition_one or board[3:9:2] == win_condition_two:
        return True

    return False


def gameon_choice():
    choice = "wrong"

    while choice not in ["Y", "N"]:
        choice = input("Would you like to keep playing? Y or N: ")

        if choice not in ["Y", "N"]:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False


def is_board_full(board):
    return board[1:-1] not in [" "] * 10


def player_marker():
    """
    OUTPUT: (Player-1-Marker, Player-2-Marker)
    """
    marker = ""

    while True:
        marker = input("Player-1, choose X or O: ").upper()
        if marker == "X" or marker == "Y":
            break

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, position, marker):
    board[position] = marker


def empty_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):

        # If any one space is empty, board is not full
        if empty_check(board, i):
            return False
    return True


def reset():
    '''
    RESETS AND RETURNS GAME VARIABLES
    '''
    is_game_active = True
    active_player = randint(0, 1)
    print(f'{list(players.values())[active_player]["name"]} goes first')
    has_won = False
    my_board = [" "] * 10

    return (is_game_active, active_player, has_won, my_board)


my_board = [" "] * 10
choices = list(range(1, 10))

active_player = randint(0, 1)
is_game_active = True
has_won = False

players = {"first": {"name": "", "marker": ""}, "second": {"name": "", "marker": ""}}

while is_game_active:
    players["first"]["name"] = input("Player-1, Enter your name: ")
    players["second"]["name"] = input("Player-2, Enter your name: ")

    players["first"]["marker"], players["second"]["marker"] = player_marker()

    print(f'{list(players.values())[active_player]["name"]} goes first')

    while not has_won:
        winner = False
        full_board = full_board_check(my_board)

        if not full_board:
            choice = user_choice()

            # Check if board space is empty

            if empty_check(my_board, choice):
                if active_player == 0:
                    place_marker(my_board, choice, players["first"]["marker"])
                else:
                    place_marker(my_board, choice, players["second"]["marker"])

                print_board(my_board)
                active_player = not active_player

            else:
                print("That slot is already taken")

            has_won = check_win_condition(my_board)

            if has_won:
                winner = not active_player
                print(
                    f"{list(players.values())[not active_player]['name']} has won the game"
                )

                if gameon_choice():
                    (is_game_active, active_player, has_won, my_board) = reset()
                else:
                    is_game_active = False

        # If board is full, ask for a new game

        else:
            print("It's a tie! ")
            if gameon_choice():
                (is_game_active, active_player, has_won, my_board) = reset()