def print_board(board):
    print(f"{board[7]} | {board[8]} | {board[9]} ")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]} ")
    print("---------")
    print(f"{board[1]} | {board[2]} | {board[3]} ")


def user_choice(choices):
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
    has_won = False

    # Row win condition

    if board[7:10] == win_condition_one or board[7:10] == win_condition_two:
        has_won = True
    elif board[4:7] == win_condition_one or board[4:7] == win_condition_two:
        has_won = True
    elif board[1:4] == win_condition_one or board[1:4] == win_condition_two:
        has_won = True

    # Column win condition

    elif board[1:10:3] == win_condition_one or board[1:10:3] == win_condition_two:
        has_won = True
    elif board[2:10:3] == win_condition_one or board[2:10:3] == win_condition_two:
        has_won = True
    elif board[3:10:3] == win_condition_one or board[3:10:3] == win_condition_two:
        has_won = True

    # Diagonal win condition

    elif board[1:10:4] == win_condition_one or board[1:10:4] == win_condition_two:
        has_won = True
    elif board[3:9:2] == win_condition_one or board[3:9:2] == win_condition_two:
        has_won = True

    return has_won


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


my_board = [" "] * 10
choices = list(range(1, 10))

active_player = 0
is_game_active = True
has_won = False

users = {"user_one": "", "user_two": ""}

while is_game_active:

    while not has_won:
        choice = user_choice(choices)
        winner = False

        if my_board[choice] == " ":
            if active_player == 0:
                my_board[choice] = "X"
                active_player = 1
            else:
                my_board[choice] = "O"
                active_player = 0
            print_board(my_board)
        else:
            print("That slot is already taken")

        has_won = check_win_condition(my_board)

        if has_won:
            winner = not active_player
            print(f"Player {winner + 1} has won the game")

            if gameon_choice():
                is_game_active = True
                active_player = 0
                has_won = False
                my_board = [" "] * 10
            else:
                is_game_active = False
