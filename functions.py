import random
import time


def update_board(row_a, row_b, row_c):
    """ updates the single rows in a board after a players turn"""
    # print board as string for aesthetic reasons
    board = f"  1 2 3\n" \
            f"A{row_a[0]}{row_a[1]}{row_a[2]}\n" \
            f"B{row_b[0]}{row_b[1]}{row_b[2]}\n" \
            f"C{row_c[0]}{row_c[1]}{row_c[2]}"
    print(board)


def player_1_turn(row_a, row_b, row_c):
    """function for Player 1 turn, includes manual user input and translation of input to position on board"""
    print("Player 1️⃣ it's your turn!")
    player_1 = input("Enter Coordinates for your move: ")
    # translate players turn into list items, to change board
    # transform string input in number and subtract 1 to transform to list index
    try:
        index_1 = int(player_1[1]) - 1
    # catch if no number was entered or sign instead
    except ValueError:
        print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
        player_1_turn(row_a, row_b, row_c)
    else:
        # determine selected row and change list item to player sign
        if player_1[0] == "A" and row_a[index_1] == "⬜️":
            row_a[index_1] = "❌"
        elif player_1[0] == "B" and row_b[index_1] == "⬜️":
            row_b[index_1] = "❌"
        elif player_1[0] == "C" and row_c[index_1] == "⬜️":
            row_c[index_1] = "❌"
        else:
            print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
            player_1_turn(row_a, row_b, row_c)


def player_2_turn(row_a, row_b, row_c):
    """function for Player 1 turn, includes manual user input and translation of input to position on board"""
    print("Player 2️⃣ it's your turn!")
    player_2 = input("Enter Coordinates for your move: ")
    try:
        index_2 = int(player_2[1]) - 1
    except ValueError:
        print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
        player_2_turn(row_a, row_b, row_c)
    else:
        if player_2[0] == "A" and row_a[index_2] == "⬜️":
            row_a[index_2] = "⭕"
        elif player_2[0] == "B" and row_b[index_2] == "⬜️":
            row_b[index_2] = "⭕"
        elif player_2[0] == "C" and row_c[index_2] == "⬜️":
            row_c[index_2] = "⭕"
        else:
            print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
            player_2_turn(row_a, row_b, row_c)


def is_winning(row_a, row_b, row_c, game_mode):
    """ checks if any possible winning combination is present, ends the game if this is true"""
    # all possible winning combinations in dictionary for easier looping
    winning = {
        "row_1": row_a,
        "row_2": row_b,
        "row_3": row_c,
        "col_1": [row_a[0], row_b[0], row_c[0]],
        "col_2": [row_a[1], row_b[1], row_c[1]],
        "col_3": [row_a[2], row_b[2], row_c[2]],
        "diagonal_1": [row_a[0], row_b[1], row_c[2]],
        "diagonal_2": [row_a[2], row_b[1], row_c[0]]
    }
    # loop through all possible combinations in dictionary
    #  check if one player has a combination (if all items in list are equal to players mark)
    for combination in winning:
        if all(fields == "❌" for fields in winning[combination]):
            print("🎉Player 1️⃣ wins the game.🎉")
            return True
        elif all(fields == "⭕" for fields in winning[combination]):
            if game_mode == "p":
                print("🎉Player 2️⃣ wins the game.🎉")
            elif game_mode == "c":
                print("😔Computer 🖥️ wins the game.😔")
            return True


def board_full(row_a, row_b, row_c):
    """ checks if board is full and no more moves possible, ends game if true"""
    if all(fields != "⬜️" for fields in row_a) and \
            all(fields != "⬜️" for fields in row_b) and \
            all(fields != "⬜️" for fields in row_c):
        print("🤷‍♀️No more moves possible. It's a draw!🤷‍♀️")
        return True


def computer_random_choice(row_a, row_b, row_c):
    # list of all possible combinations to let computer choose randomly if player is not about to win
    possible_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    computer_choice = random.choice(possible_moves)
    index = int(computer_choice[1]) - 1
    if computer_choice[0] == "A" and row_a[index] == "⬜️":
        row_a[index] = "⭕"
    elif computer_choice[0] == "B" and row_b[index] == "⬜️":
        row_b[index] = "⭕"
    elif computer_choice[0] == "C" and row_c[index] == "⬜️":
        row_c[index] = "⭕"
    else:
        computer_random_choice(row_a, row_b, row_c)


def computer_turn(row_a, row_b, row_c):
    """lets the computer play, either choose random move, is player is not about to win or hinders player to win"""
    print("The 🖥️ is playing.")
    diagonals = {
        "diagonal_1": [row_a[0], row_b[1], row_c[2]],
        "diagonal_2": [row_a[2], row_b[1], row_c[0]]
    }
    # checks if Player is about to win by checking if there is a combination that is only missing one cross
    if row_a.count("⬜️") == 1 and row_a.count("❌") == 2:
        for i in range(len(row_a)):
            if row_a[i] == "⬜️":
                row_a[i] = "⭕"
                print("row_a")
    elif row_b.count("⬜️") == 1 and row_b.count("❌") == 2:
        for i in range(len(row_b)):
            if row_b[i] == "⬜️":
                row_b[i] = "⭕"
                print("row_b")
    elif row_c.count("⬜️") == 1 and row_c.count("❌") == 2:
        for i in range(len(row_c)):
            if row_c[i] == "⬜️":
                row_c[i] = "⭕"
                print("row_c")
    elif row_a[0] == "⬜️" and row_b[0] == "❌" and row_c[0] == "❌":
        row_a[0] = "⭕"
    elif row_b[0] == "⬜️" and row_a[0] == "❌" and row_c[0] == "❌":
        row_b[0] = "⭕"
    elif row_c[0] == "⬜️" and row_b[0] == "❌" and row_a[0] == "❌":
        row_c[0] = "⭕"
    elif row_a[1] == "⬜️" and row_b[1] == "❌" and row_c[1] == "❌":
        row_a[1] = "⭕"
    elif row_b[1] == "⬜️" and row_a[1] == "❌" and row_c[1] == "❌":
        row_b[1] = "⭕"
    elif row_c[1] == "⬜️" and row_b[1] == "❌" and row_a[1] == "❌":
        row_c[1] = "⭕"
    elif row_a[2] == "⬜️" and row_b[2] == "❌" and row_c[2] == "❌":
        row_a[2] = "⭕"
    elif row_b[2] == "⬜️" and row_a[2] == "❌" and row_c[2] == "❌":
        row_b[2] = "⭕"
    elif row_c[2] == "⬜️" and row_b[2] == "❌" and row_a[2] == "❌":
        row_c[2] = "⭕"
    elif row_a[0] == "⬜️" and row_b[1] == "❌" and row_c[2] == "❌":
        row_a[0] = "⭕"
    elif row_b[1] == "⬜️" and row_a[0] == "❌" and row_c[2] == "❌":
        row_b[1] = "⭕"
    elif row_c[2] == "⬜️" and row_a[0] == "❌" and row_b[1] == "❌":
        row_c[2] = "⭕"
    elif row_a[2] == "⬜️" and row_b[1] == "❌" and row_c[0] == "❌":
        row_a[2] = "⭕"
    elif row_b[1] == "⬜️" and row_a[2] == "❌" and row_c[0] == "❌":
        row_b[1] = "⭕"
    elif row_c[0] == "⬜️" and row_a[2] == "❌" and row_b[1] == "❌":
        row_c[0] = "⭕"
    else:
        computer_random_choice(row_a, row_b, row_c)
