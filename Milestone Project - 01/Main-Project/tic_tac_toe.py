# Tic-Tac-Toe Game

# The function to print board of Tic-Tac-Toe Game
def print_board(board):
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