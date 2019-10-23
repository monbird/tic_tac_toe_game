
# ------------------------------------->     GAME     <-------------------------------------

import re


# check if player has won
def check_score(board):
    # variable initialization
    is_winner = False
    who_won = None

    # Horizontal check:
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][0] != " ":
            is_winner = True
            who_won = board[row][0]
            break

    # Vertical check:
    for column in range(3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column] and board[0][column] != " ":
            is_winner = True
            who_won = board[0][column]
            break

    # Diagonal check:
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ":
        is_winner = True
        who_won = board[0][0]

    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != " ":
        is_winner = True
        who_won = board[0][2]

    return is_winner, who_won


# insert mark at chosen position
def insert_player(board, player_coordinates, player):
    # split the user input coordinates to get row and column separately
    coordinates_list = player_coordinates.split(",")
    # take into account indexing from zero by subtracting 1
    row = int(coordinates_list[0]) - 1
    column = int(coordinates_list[1]) - 1

    # check position availability, if available place a mark on the board and draw updated board
    if board[row][column] == " ":
        board[row][column] = player
        draw_a_board_game(board)
        return True
    else:
        return False


# function that asks for user position
def ask_for_position(player, board):
    player_coordinates = ""
    # regexp check for correct input format, ask until correct
    while not re.search("^[1-3], ?[1-3]$", player_coordinates):
        player_coordinates = input("\nWhat is your move Mr {} (row, col)? ".format(player))

    # try to insert letter at chosen position
    inserted = insert_player(board, player_coordinates, player)
    # if position is taken ask for another position
    if not inserted:
        print("This position is already taken. Choose another position.")
        return ask_for_position(player, board)

    # return updated board (including users move)
    return board


# board drawing function
def draw_a_board_game(board):
    board_flat_list = []

    # board flattening list of list
    for row in board:
        for element in row:
            board_flat_list.append(element)

    # board visualization for the user
    print("\n {} | {} | {} \n--- --- --- \n {} | {} | {} \n--- --- --- \n {} | {} | {} \n".format(*board_flat_list))


# main function of the game
def play():
    print("Welcome to Tic Tac Toe game.")
    # empty board initialization
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    # call the board drawing function (shows empty board at the start)
    draw_a_board_game(board)

    # ask user which letter they want to be
    player1 = ""
    while player1 not in ("X", "O"):
        player1 = input("\nPlayer 1 do you want to be 'X' or 'O'? ").upper()

    # second player is automatically the other letter
    player2 = ""
    if player1 == "O":
        player2 = "X"
        print("Player 2 you are 'X' then.")
    else:
        player2 = "O"
        print("Player 2 you are 'O' then.")

    # ask player1 for a first position
    updated_board = ask_for_position(player1, board)

    # variable initialization
    is_winner = False
    who_won = None

    # ask each user for a new position until board is full
    for i in range(4):
        for player in [player2, player1]:
            # ask for position
            updated_board = ask_for_position(player, updated_board)
            # after move check for winner
            is_winner, who_won = check_score(updated_board)
            # if someone wins stop asking for more moves even if the board is still not full
            if is_winner:
                break
        if is_winner:

            break

    # depending on the score show appropriate message to the user/s
    if is_winner:
        print("Congratulations, {}'s has won the game!".format(who_won))
    else:
        print("No winner this time.")

    # ask users if they want to play again
    play_again = ""
    while play_again not in ("yes", "no"):
        play_again = input("Would you like to play again (yes/no)? ")

    # if want to play - resume the game, otherwise end it
    if play_again == "yes":
        return play()

    print("Bye bye!")


if __name__ == '__main__':
    play()
