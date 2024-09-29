import score


def main():
    """Main program function"""
    print("Welcome to the Score Processing Program!")
    # Get initial valid score
    score = get_valid_score()
    # Menu loop condition
    quit_program = False
    # Main menu loop
    # Make function for display_menu(): to fit in with choice.
    while choice != "Q":
        display_menu()
        choice = input("Enter your choice: ").upper()


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive"""
    valid_score = int(input("Enter a score between 0 and 100: "))
    while valid_score < 0 or valid_score > 100:
        print("Score must be between 0 and 100")
        valid_score = int(input("Enter a score between 0 and 100: "))
    return valid_score


def print_result(user_score):
    """Print the result bases on the score"""
    result = score.evaluate_score(user_score)
    print(f"Result for {user_score}: {result}")


def display_menu():
    """Display the menu options"""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def show_stars(user_score):
    """Print stars based on the user score"""
    print(f"Stars for score {user_score}: {'*' * user_score}")

if __name__ == "__main__":
    main()
