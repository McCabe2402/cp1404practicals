"""
Word Occurrences
Estimate: 10 minutes
Actual:
"""


def main():
    user_input = input("Enter a string: ")
    counts = count_word_occurrences(user_input)
    for word, count in counts.items():
        print(f"{word} : {count}")


def count_word_occurrences(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__ == "__main__":
    main()
