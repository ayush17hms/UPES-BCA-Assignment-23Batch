# game
board = [ "-",  "-",  "-",
          "-",  "-",  "-",
          "-",  "-",  "-" ]


game_is_still_going = True

winner = None
current_player = "X"

# display board
def print_board():
    print(board[0] +  "|"  + board[1] +  "|"  + board[2])
    print(board[3] +  "|"  + board[4] +  "|"  + board[5])
    print(board[6] +  "|"  + board[7] +  "|" + board[8])
    print("Ayush kumar jha, 500086400")

def play_game():
    
    print_board()

    
    while game_is_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # game has ended
    if winner == "X" or winner == "O":
        print(winner, "won.")
    elif winner == None:
        print("Tie.")

def handle_turn(player):

    print("It's " + player + "'s turn.")
    position = input("choose a position 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
         position = input("Ivalid input. choose a position 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Already chosen, select other position ")

    board[position] = player
    print_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner   # call the global winner
    row_winner = check_rows()
    # check columns
    column_winner = check_column()
    # check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None

    return

def check_rows():
     # call the global game_is_still_going variable
    global game_is_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_still_going = False
    # return the winner (X or O)
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_column():
     # call the global game_is_still_going variable
    global game_is_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_is_still_going = False
    # return the winner (X or O)
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    # call the global game_is_still_going variable
    global game_is_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        game_is_still_going = False
    # return the winner (X or O)
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return

def check_if_tie():
    global game_is_still_going

    if "-" not in board:
        game_is_still_going = False
    return

def flip_player():
    global current_player  # call current_player

    # check the current player and then change it
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
play_game()
