def main():
    """Main function to run the program"""
    count = 5
    numbers = get_numbers(count)
    minimum, maximum, total_sum, count = calculate_statistics(numbers)
    display_statistics(minimum, maximum, total_sum, count)

def get_numbers(count):
    """Prompt the user to enter a specified number of numbers"""
    numbers = []
    for i in range(count):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)
    return numbers

def calculate_statistics(numbers):
    """Calculate and return the minimum, maximum, sum, and count of the numbers."""
    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)
    count = len(numbers)
    return minimum, maximum, total_sum, count

def display_statistics(minimum, maximum, total_sum, count):
    """"Display the calculated statistics"""
    print("Information about the numbers:")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Sum: {total_sum}")
    print(f"Count: {count}")

if __name__ == '__main__':
    main()