import art
from utils import initialize_board, print_board, check_winner, display_invalid_input

title_art = art.title

def validate_move(move, board):
    if move not in board:
        display_invalid_input("Input not recognized. Please enter a number from 1 to 9.")
        return False
    if board[move] != ' ':
        display_invalid_input("That space is already occupied. Try another move.")
        return False
    return True

def main():
    board = initialize_board()
    current_player = 'X'
    for turn in range(9):
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ").strip()
        
        # Validate input using the new function
        if not validate_move(move, board):
            continue
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print_board(board)
        print("It's a draw!")

if __name__ == "__main__":
    main()
