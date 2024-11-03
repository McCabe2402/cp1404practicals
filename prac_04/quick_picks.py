import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Main function to ask user for number of picks and generate them."""
    try:
        num_picks = int(input("How many quick picks would like to generate? "))
        if num_picks < 1:
            print("Please select a positive number.")
            return

        for i in range(num_picks):
            quick_pick = generate_quick_pick()
            print(f"Quick pick {i + 1}: {sorted(quick_pick)}")

    except ValueError:
        print("Invalid input. Please enter a whole number")


def generate_quick_pick():
    """Generate a single quick pick containing 6 unique random number."""
    return random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)


if __name__ == "__main__":
    main()
