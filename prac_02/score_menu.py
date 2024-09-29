import score


def main():
    """Main program function"""
    print("Welcome to the Score Processing Program!")
    # Get initial valid score
    input_score = get_valid_score()
    # Get user choice
    # Main menu loop
    display_menu()
    # Make function for display_menu(): to fit in with choice.
    while choice != "Q":
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            print_result(input_score)
        elif choice == "S":
            show_stars(input_score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Invalid choice!")



def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive"""
    valid_score = int(input("Enter a score between 0 and 100: "))
    while valid_score < 0 or valid_score > 100:
        print("Score must be between 0 and 100")
        valid_score = int(input("Enter a score between 0 and 100: "))
    return valid_score


def print_result(input_score):
    """Print the result bases on the score"""
    result = score.evaluate_score(input_score)
    print(f"Result for {input_score}: {result}")


def display_menu():
    """Display the menu options"""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def show_stars(input_score):
    """Print stars based on the user score"""
    print(f"Stars for score {input_score}: {'*' * input_score}")

if __name__ == "__main__":
    main()
