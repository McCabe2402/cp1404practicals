# Get the user's name
name = input("Enter your name: ")


# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("H - Say Hello")
    print("G - Say Goodbye")
    print("Q - Quit")


# Loop until the user enters 'Q'
choice = ''
while choice != 'Q':
    # Display the menu and get the user's choice
    display_menu()
    choice = input("Enter your choice: ").upper()

    if choice == 'H':
        print(f"Hello, {name}")
    elif choice == 'G':
        print(f"Goodbye, {name}")
    elif choice == 'Q':
        print("Thank you! Finished!")
    else:
        print("Invalid choice, please try again!")