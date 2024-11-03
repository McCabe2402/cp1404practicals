from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")

    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        name = input("Name: ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_status = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} worth ${guitar.cost:,.2f} {vintage_status}")


if __name__ == "__main__":
    main()
