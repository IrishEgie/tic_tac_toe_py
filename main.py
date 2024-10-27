from art import title
from utils import clear_console
from game import pvp_ttt
from menu import display_menu

def main():
    while True:
        clear_console()  # Clear the console at the beginning of each loop
        print(title)
        display_menu()
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            pvp_ttt()  # This will show the game state
        elif choice == '2':
            print("Playing against the bot is not implemented yet.")
        elif choice == '3':
            print("Thanks for playing!")
            break  # Exit the loop and quit the program
        else:
            print("Invalid option. Please select 1, 2, or 3.")
        
        input("Press Enter to continue...")  # Wait for user input before clearing the console again

if __name__ == "__main__":
    main()
