# Tic-Tac-Toe Game

# Global variables
board = [' '] * 10 
current_player = 1
player_1_sign = ''
player_2_sign = ''

# Guide
def show_guide():
    print("Guide for the position of different blocks in the board.")
    print("\n   |   |   ")
    print(" 7 | 8 | 9 ")
    print("___|___|___")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("   |   |   \n")
    print("Press these numeric values whenever you're asked to choose the position of your X/O for the respective positions.\n")

# Function to print the current board
def print_board():
    print("Your Board")
    print("\n   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   \n")

# Function to ask players what they want to choose
def user_choice():
    global player_1_sign, player_2_sign
    while True:
        sign = input("Choose a sign you want to take 'X' or 'O': ").upper()
        if sign in ['X', 'O']:
            break
        else:
            print("Invalid Input! Please choose 'X' or 'O'.")
    
    if sign == 'X':
        player_1_sign = 'X'
        player_2_sign = 'O'
    else:
        player_1_sign = 'O'
        player_2_sign = 'X'
    
    print(f"Player-1 is {player_1_sign}")
    print(f"Player-2 is {player_2_sign}")

# Function to choose who goes first
def choose_first_player():
    global current_player
    while True:
        want = input("Player-1, do you want to start first (Y/N): ").upper()
        if want in ['Y', 'YES']:
            current_player = 1
            print("Player-1 goes first")
            break
        elif want in ['N', 'NO']:
            current_player = 2
            print("Player-2 goes first")
            break
        else:
            print("Invalid Input! Please enter Y or N.")

# Function to check if a position is available
def is_space_free(position):
    return board[position] == ' '

# Function to place a mark on the board
def place_marker(position, mark):
    board[position] = mark

# Function to check for a winner
def check_winner():
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  
        [1, 5, 9], [3, 5, 7]              
    ]
    
    for combo in winning_combinations:
        if (board[combo[0]] == board[combo[1]] == board[combo[2]] != ' '):
            return board[combo[0]]
    return None

# Function to check if the board is full
def is_board_full():
    return ' ' not in board[1:10]

# Function to get player's move
def is_valid_input(user_input):
    return user_input.isdigit() and 1 <= int(user_input) <= 9

def get_player_move(player_num):
    while True:
        position_str = input(f"Player {player_num}, enter position (1-9): ")
        
        if is_valid_input(position_str):
            position = int(position_str)
            if is_space_free(position):
                return position
            else:
                print("That position is already taken. Choose another.")
        else:
            print("Please enter a number between 1 and 9.")

# Main game function
def play_game():
    global current_player
    
    show_guide()
    print_board()
    user_choice()
    choose_first_player()
    
    game_running = True
    
    while game_running:
        print_board()
        
        if current_player == 1:
            current_sign = player_1_sign
        else:
            current_sign = player_2_sign
        
        position = get_player_move(current_player)
        place_marker(position, current_sign)
        
        winner = check_winner()
        if winner:
            print_board()
            if winner == player_1_sign:
                print("Player-1 wins!")
            else:
                print("Player-2 wins!")
            game_running = False
        elif is_board_full():
            print_board()
            print("It's a tie!")
            game_running = False
        else:
            current_player = 2 if current_player == 1 else 1

# Function to ask if players want to play again
def play_again():
    while True:
        choice = input("Do you want to play again? (Y/N): ").upper()
        if choice in ['Y', 'YES']:
            return True
        elif choice in ['N', 'NO']:
            return False
        else:
            print("Please enter Y or N.")

# Starting the game
def main():
    print("Welcome to Tic-Tac-Toe! \n")
    
    while True:
        # Reset
        board = [' '] * 10
        play_game()
        
        if not play_again():
            print("Thanks for playing! Goodbye! ")
            break
main()