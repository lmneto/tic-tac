import sys

#board structure
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#printing the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#global there_is_winner
#there_is_winner = 0
playing_game = 1
winner = None

def start_game():
    player = 0              #by default starting with player 0 that plays with O
    print_board()           #printing the board at first

    while playing_game:
        #check game over
        check_for_winner()

        if winner == "X" or winner == "O":
            print("won the game.")

        choose_position(player)
        if player == 0:
            player = 1

        else:
            player = 0
        #next player

def choose_position(player):
    if player == 1:
        print("\n---------Player X turn---------\n")

    else:
        print("\n---------Player O turn---------\n")
    position = input("\nChoose position to play [1-9] or 0 to exit Game: ")

    while position not in ["1", "2", "3","4", "5", "6","7", "8", "9", "0"]:         #making sure option is in scope
        print("Position invalid")
        position = input("\nChoose position to play [1-9] or 0 to exit Game: ")

    if int(position) == 0:
        sys.exit()

    position = int(position) - 1

    if player == 1:
        board[position] = "X"
    #    player = 0
    else:
        board[position] = "O"
    #    player = 1

    print_board()                #after choosing position print board with new result

def check_for_winner():
    #checking rows, columns and diagonals
    check_rows()
    check_columns()
    check_diagonals()
#    check_board_full()
    return

def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"    #Boolean True if all line has same sign and different from -
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if row_1 or row_2 or row_3:
    #    there_is_winner=1

    if row_1:
        print("Player " + name_player1 + board[0] + " won")
        sys.exit()

    if row_2:
        print("Player " + name_player1 + board[3] + " won")
        sys.exit()

    if row_3:
        print("Player " + name_player1 + board[6] + " won")
        sys.exit()

    return


def check_columns():
    column_1 = board[0] == board[3] == board[6] != "-"      #Boolean True if all column has same sign and different from -
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if column_1 or column_2 or column_3:
    #    there_is_winner=1

    if column_1:
        print("Player " + name_player1 + board[0] + " won")
        sys.exit()

    if column_2:
        print("Player " + name_player1 + board[1] + " won")
        sys.exit()

    if column_3:
        print("Player " + name_player1 + board[2] + " won")
        sys.exit()


    return

def check_diagonals():
    diagonal_1 = board[0] == board[4] == board[8] != "-"    #Boolean True if all diagonal has same sign and different from -
    diagonal_2 = board[2] == board[4 ] == board[6] != "-"

    if diagonal_1:
        print("Player " + name_player1 + board[0] + " won")
        sys.exit()

    if diagonal_2:
        print("Player " + name_player2 + board[2] + " won")
        sys.exit()

    return

#def check_board_full():
#    if board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8]:
#       print("\nGame was a Draw\n")

if __name__ == '__main__':
    print("Starting game")          #starting main menu
    choice = input("You have two options:\n       1 - Start Game\n       2 - Exit\n\n\nOption: ")

    if choice == '2':           #If player wants to end the game from main menu
        print("the end")
        sys.exit()

    if choice == '1':
        name_player1 = input("\nName Player1: \n")      #Naming player 1
        name_player2 = input("\nName Player2: \n")      #Naming player 2
        start_game()

