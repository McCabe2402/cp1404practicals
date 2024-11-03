import random


def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    # Generate a random score between 0 and 100
    random_score = random.uniform(0, 100)
    print(random_score)
    random_result = evaluate_score(random_score)
    print(random_result)


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Fail"


if __name__ == "__main__":
    main()
