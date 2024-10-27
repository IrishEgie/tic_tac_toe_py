from utils import initialize_board, print_board, check_winner, validate_move, display_invalid_input
import random
from art import title

def pvp_ttt():
    board = initialize_board()
    current_player = 'X'
    for turn in range(9):
        print(title)  # Display title art each turn
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ").strip()

        if move.lower() == 'q':
            print("Returning to the main menu...")
            return  # Exit the game function and return to the main menu

        if not validate_move(move, board):
            # Call display_invalid_input to show the error message
            display_invalid_input("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print_board(board)
        print("It's a draw!")

def pve_ttt():
    board = initialize_board()
    current_player = 'X'  # Player is 'X', computer is 'O'
    
    for turn in range(9):
        print(title)  # Display title art each turn
        print_board(board)
        
        if current_player == 'X':
            move = input(f"Player {current_player}, enter your move (1-9) or 'q' to quit: ").strip()

            if move.lower() == 'q':
                print("Returning to the main menu...")
                return  # Exit the game function and return to the main menu

            if not validate_move(move, board):
                display_invalid_input("Invalid move. Try again.")
                continue
            
            board[move] = current_player
        else:
            # Computer's turn
            available_moves = [k for k, v in board.items() if v == ' ']
            move = random.choice(available_moves)  # Choose a random available move
            print(f"Computer chooses: {move}")
            board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print_board(board)
        print("It's a draw!")