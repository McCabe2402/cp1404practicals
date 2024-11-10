def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(min_length):
    user_password = input("Enter your password: ")
    while len(user_password) < min_length:
        print('Password must be at least 8 characters long.')
        user_password = input('Enter a password: ')
    return user_password


if __name__ == '__main__':
    main()
