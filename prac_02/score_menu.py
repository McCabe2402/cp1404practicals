import score

def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive"""
    score = int(input("Enter a score between 0 and 100: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter a score between 0 and 100: "))
    return score