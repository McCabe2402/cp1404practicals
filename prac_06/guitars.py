from guitar import Guitar

def main():
    guitars = []

    name = ""

    while name != "":
        name = input("Enter the name of the guitar (or press enter to finish): ")

        if name:
            year = int(input("Enter the year of the guitar (or press enter to finish): "))
            cost = float(input("Enter the cost of the guitar (or press enter to finish): "))

            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

    print("\nYour guitars:")
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()