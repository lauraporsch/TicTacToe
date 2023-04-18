# Using lists to create interactive board
row_a = ["⬜️", "⬜️", "⬜️"]
row_b = ["⬜️", "⬜️", "⬜️"]
row_c = ["⬜️", "⬜️", "⬜️"]


# print board as string for aesthetic reasons
def update_board():
    board = f"  1 2 3\n" \
            f"A{row_a[0]}{row_a[1]}{row_a[2]}\n" \
            f"B{row_b[0]}{row_b[1]}{row_b[2]}\n" \
            f"C{row_c[0]}{row_c[1]}{row_c[2]}"
    print(board)
    return board


# Create turns for players
def player_1_turn():
    print("Player 1 it's your turn!")
    player_1 = input("Enter Coordinates for your move: ")
    # translate players turn into list items, to change board
    # transform string input in number and subtract 1 to transform to list index
    index_1 = int(player_1[1]) - 1
    # determine selected row and change list item to player sign
    if player_1[0] == "A" and row_a[index_1] == "⬜️":
        row_a[index_1] = "❌"
    elif player_1[0] == "B" and row_b[index_1] == "⬜️":
        row_b[index_1] = "❌"
    elif player_1[0] == "C" and row_c[index_1] == "⬜️":
        row_c[index_1] = "❌"
    else:
        print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
        player_1_turn()


def player_2_turn():
    print("Player 2 it's your turn!")
    player_2 = input("Enter Coordinates for your move: ")

    index_2 = int(player_2[1]) - 1
    if player_2[0] == "A" and row_a[index_2] == "⬜️":
        row_a[index_2] = "⭕"
    elif player_2[0] == "B" and row_b[index_2] == "⬜️":
        row_b[index_2] = "⭕"
    elif player_2[0] == "C" and row_c[index_2] == "⬜️":
        row_c[index_2] = "⭕"
    else:
        print("Invalid choice. The field is either taken or doesn't exist. Please try again.")
        player_2_turn()


def is_winning():
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
            print("Player 1 wins the game.")
            return True
        elif all(fields == "⭕" for fields in winning[combination]):
            print("Player 2 wins the game.")
            return True


# check if game is done, because no more moves possible/board full
def board_full():
    if all(fields != "⬜️" for fields in row_a) and \
            all(fields != "⬜️" for fields in row_b) and \
            all(fields != "⬜️" for fields in row_c):
        print("No more moves possible. It's a draw!")
        return True


print("Hello, welcome to Tic Tac Toe.")
print("A1 A2 A3\n"
      "B1 B2 B3\n"
      "C1 C2 C3\n")
print("To choose a field, simply enter the coordinates as shown on the example board above.")

game_is_on = True
# keep game going until either someone is winning or the board is full
while game_is_on:
    player_1_turn()
    current_board = update_board()
    if is_winning():
        game_is_on = False
        break
    elif board_full():
        game_is_on = False
        break
    player_2_turn()
    current_board = update_board()
    if is_winning():
        game_is_on = False
    elif board_full():
        game_is_on = False



