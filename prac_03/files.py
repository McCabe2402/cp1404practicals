# Question 1: Using read()
def read_file_with_read():
    with open('example.txt', 'r') as file:
        content = file.read()
        print("Content of the file using read():")
        print(content)

# Question 2: Using readline()
def read_file_with_readline():
    with open('example.txt', 'r') as file:
        print("Content of the file using readline():")
        line = file.readline()
        while line:
            print(line.strip())
            line = file.readline()

# Question 3: Using read_lines()
def read_file_with_read_lines():
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print("Content of the file using readlines():")
        for line in lines:
            print(line.strip())

# Question 4: Using for line in file
def read_file_with_for_loop():
    with open('example.txt', 'r') as file:
        print("Content of the file using for line in file:")
        for line in file:
            print(line.strip())

# Question 5: Writing to a file
def write_name_to_file():
    name = input("Please enter your name: ")
    with open('name.txt', 'w') as file:
        file.write(name)
    print(f"Your name '{name}' has been written to name.txt.")

# Question 6: Read from name.txt and print greeting
def greet_user_from_file():
    with open('name.txt', 'r') as file:
        name = file.read().strip()
    print(f"Your name '{name}' has been written to name.txt.")

# Question 7: Read first two number from numbers.txt and print their sum
def sum_first_two_numbers():
    with open('numbers.txt', 'r') as file:
        first_number = int(file.readline().strip())
        second_number = int(file.readline().strip())
        result = first_number + second_number
    print(f"The sum of the first two numbers is: {result}")

if __name__ == "__main__":
    # Uncomment the function you want to test
    # read_file_with_read()
    # read_file_with_readline()
    # read_file_with_read_lines()
    # read_file_with_for_loop()
    # write_name_to_file()
    # greet_user_from_file()
    sum_first_two_numbers()
