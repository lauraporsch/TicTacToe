from functions import update_board, player_1_turn, player_2_turn, is_winning, board_full, computer_turn


def play_game():
    # Using lists to create interactive board
    game_mode = input("To play against the computer type 'c' to play against another player, type 'p'  ").lower()
    row_a = ["⬜️", "⬜️", "⬜️"]
    row_b = ["⬜️", "⬜️", "⬜️"]
    row_c = ["⬜️", "⬜️", "⬜️"]

    game_is_on = True
    # keep game going until either someone is winning or the board is full
    while game_is_on:
        player_1_turn(row_a, row_b, row_c)
        update_board(row_a, row_b, row_c)
        if is_winning(row_a, row_b, row_c, game_mode):
            game_is_on = False
            break
        elif board_full(row_a, row_b, row_c):
            game_is_on = False
            break
        if game_mode == "p":
            player_2_turn(row_a, row_b, row_c)
        elif game_mode == "c":
            computer_turn(row_a, row_b, row_c)
        update_board(row_a, row_b, row_c)
        if is_winning(row_a, row_b, row_c, game_mode):
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
print("To choose a field, simply enter the coordinates as shown on the example board above.\n")

play_game()





