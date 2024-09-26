score = float(input("Enter score: "))
# Changed to format both possible out of bounds.

def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Fail"
