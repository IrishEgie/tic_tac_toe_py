import art
from utils import initialize_board, print_board, check_winner, display_invalid_input
from menu import display_menu

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
    # Display the menu
    display_menu()
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == '1':
        board = initialize_board()
        current_player = 'X'
        for turn in range(9):
            print(title_art)  # Display title art each turn
            print_board(board)
            move = input(f"Player {current_player}, enter your move (1-9): ").strip()
            
            if not validate_move(move, board):
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
    
    elif choice == '2':
        print("Playing against the bot is not implemented yet.")
    
    elif choice == '3':
        print("Thanks for playing!")
    
    else:
        print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
