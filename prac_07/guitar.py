import csv


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar instance."""
        return f"{self.name} {self.year} : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the Guitar."""
        return current_year - self.year

    def is_vintage(self):
        """Return true if the guitar is 50 or more years old"""
        return self.get_age(2024) >= 50


def main():
    file_name = "guitars.csv"
    guitars = read_guitars_from_csv(file_name)
    guitars.sort(key=lambda guitar: guitar.year)
    display_guitars(guitars)


def read_guitars_from_csv(file_name):
    """Reads guitar data from a CSV file and returns a list of Guitar objects."""
    guitars = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
        return guitars


def display_guitars(guitars):
    """Displays all guitars in the list."""
    for guitar in guitars:
        print(guitar)
        age = guitar.get_age(2024)
        print(f"The guitar is {age} years old.")
        if guitar.is_vintage():
            print("The guitar is vintage.")
        else:
            print("The guitar is not vintage.")
        print("-" * 40)


if __name__ == "__main__":
    main()
