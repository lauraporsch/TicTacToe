import os

from termcolor import colored, cprint
os.system('color')

def update_board(row_a, row_b, row_c):
    # print board as string for aesthetic reasons
    board = f"  1 2 3\n" \
            f"A{row_a[0]}{row_a[1]}{row_a[2]}\n" \
            f"B{row_b[0]}{row_b[1]}{row_b[2]}\n" \
            f"C{row_c[0]}{row_c[1]}{row_c[2]}"
    print(board)


# Create turns for players
def player_1_turn(row_a, row_b, row_c):
    print("Player 1️⃣ its your turn!")
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


def is_winning(row_a, row_b, row_c):
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
            print("🎉Player 2️⃣ wins the game.🎉")
            return True


# check if game is done, because no more moves possible/board full
def board_full(row_a, row_b, row_c):
    if all(fields != "⬜️" for fields in row_a) and \
            all(fields != "⬜️" for fields in row_b) and \
            all(fields != "⬜️" for fields in row_c):
        print("🤷‍♀️No more moves possible. It's a draw!🤷‍♀️")
        return True


def play_game():
    # Using lists to create interactive board
    row_a = ["⬜️", "⬜️", "⬜️"]
    row_b = ["⬜️", "⬜️", "⬜️"]
    row_c = ["⬜️", "⬜️", "⬜️"]
    game_is_on = True
    # keep game going until either someone is winning or the board is full
    while game_is_on:
        player_1_turn(row_a, row_b, row_c)
        update_board(row_a, row_b, row_c)
        if is_winning(row_a, row_b, row_c):
            game_is_on = False
            break
        elif board_full(row_a, row_b, row_c):
            game_is_on = False
            break
        player_2_turn(row_a, row_b, row_c)
        update_board(row_a, row_b, row_c)
        if is_winning(row_a, row_b, row_c):
            game_is_on = False
        elif board_full(row_a, row_b, row_c):
            game_is_on = False
    go_again = input("Would you like to play again? Type yes or no  ").lower()
    if go_again == "yes":
        play_game()
    else:
        print("Thank you for playing!")


print("Hello, welcome to Tic Tac Toe.")
print("A1 A2 A3\n"
      "B1 B2 B3\n"
      "C1 C2 C3\n")
print("To choose a field, simply enter the coordinates as shown on the example board above.")

play_game()





