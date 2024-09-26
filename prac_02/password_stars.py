def main():
    password = input('Enter a password: ')
    MIN_LENGTH = 8
    while len(password) < MIN_LENGTH:
        print('Password must be at least 8 characters long.')
        password = input('Enter a password: ')

    print("*" * len(password))

if __name__ == '__main__':
    main()