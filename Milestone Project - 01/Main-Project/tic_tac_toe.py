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
def print_board(board):
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
print_board([])

# Function to ask player_a what he/she wants to choose
def user_choice(sign):
    sign = input("Choose a sign you want to take 'X' or 'O': ")
    if sign == 'X' or sign == 'x':
        sign = 'X'
    elif sign == 'O' or sign == 'o':
        sign = 'O'
    # print("You choosed",sign)
    if sign == 'X':
        player_1 = 'X'
        player_2 = 'O'
    else:
        player_1 = 'O'
        player_2 = 'X'
    print("Player-1 is",player_1)
    print("Player-2 is",player_2)
user_choice([])

# 