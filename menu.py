def display_menu():
    menu_options = [
        "1. Play with local friend",
        "2. Play with bot",
        "3. Quit"
    ]
    
    # Determine the width for the rectangle
    width = max(len(option) for option in menu_options) + 4  # Add padding for the rectangle
    
    # Print the top border
    print('#' * width)
    
    # Print each option centered within the rectangle
    for option in menu_options:
        print(f"# {option:<{width - 3}} #")  # Align left with padding
    
    # Print the bottom border
    print('#' * width)

# Call the menu display function
if __name__ == "__main__":
    display_menu()
