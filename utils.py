import os

def initialize_board():
    return {str(i): ' ' for i in range(1, 10)}  # Initialize with keys from 1 to 9

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_console()  # Clear the console before printing the board
    title_lines = art.title.strip().splitlines()
    # Print title and grid in one row
    print(f"{title_lines[0]}  1 | 2 | 3")
    print(f"{title_lines[1]} -----------")
    print(f"{title_lines[2]} 4 | 5 | 6")
    print(f"{title_lines[3]} -----------")
    print(f"{title_lines[4]} 7 | 8 | 9")
    print("\nRules: Players take turns to place their marks in the numbered spaces. First to align three marks wins!")
    print()
    # Display the current state of the board
    for i in range(1, 10):
        value = board[str(i)]
        if i % 3 == 1 and i != 1:  # Add horizontal separator for rows
            print("  -----------")
        print(f"  {value}", end=" |" if i % 3 != 0 else "")
        if i % 3 == 0:
            print()  # Move to the next line
    
def check_winner(board):
    # Define winning combinations using 1-9
    winning_combinations = [
        ['1', '2', '3'],  # Row 0
        ['4', '5', '6'],  # Row 1
        ['7', '8', '9'],  # Row 2
        ['1', '4', '7'],  # Column A
        ['2', '5', '8'],  # Column B
        ['3', '6', '9'],  # Column C
        ['1', '5', '9'],  # Diagonal \
        ['3', '5', '7'],  # Diagonal /
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None
