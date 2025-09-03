# Tic-Tac-Toe Game

# Guide
print("Guide for the position of different blocks in the board.")
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("\n   |   |   ")
print(" 7 | 8 | 9 ")
print("___|___|___")
print("   |   |   ")
print(" 4 | 5 | 6 ")
print("___|___|___")
print("   |   |   ")
print(" 1 | 2 | 3 ")
print("   |   |   \n")
print("Press these numeric values whenever you asked to choose the position of your X/O for the respective positions. \n")

# The function to print board of Tic-Tac-Toe Game
def print_board():
    print("Your Board")
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print("\n   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   \n")
print_board()

# Function to ask player_a what he/she wants to choose
def user_choice():
    while True:
        sign = input("Choose a sign you want to take 'X' or 'O': ")
        if sign == 'X' or sign == 'x':
            sign = 'X'
            break
        elif sign == 'O' or sign == 'o':
            sign = 'O'
            break
        else:
            print("Invalid Input! Please press key which is asked to press.")
    if sign == 'X':
        player_1 = 'X'
        player_2 = 'O'
        # break
    elif sign == 'Y':
        player_1 = 'O'
        player_2 = 'X'
        # break
    else:
        print('')
    print("Player-1 is",player_1)
    print("Player-2 is",player_2)
user_choice()

# Function to choose the first chance
def user_want():
    global current_player
    while True:
        want = input("Player-1, do you want to start first (Y/N): ")
        if want == 'Y' or want == 'y':
            current_player = 1
            print("Player-1 goes first")
            break
        elif want == 'N' or want == 'n':
            current_player = 2
            print("Player-2 goes first")
            break
        else:
            print("Invalid Input! Please press key which is asked to press.")
user_want()

# user = user_want()
# if user == 1:
#     print("Player-1")


# Main Function: To ask users to choose positions
# def user_position(num):
#     choice_bucket = [1,2,3,4,5,6,7,8,9]
#     choice = int(input(f"Enter the position of your {}"))