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


if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)
    age = my_guitar.get_age(2024)
    print(f"The guitar is {age} years old.")
    if my_guitar.is_vintage():
        print("This guitar is vintage")
    else:
        print("This guitar is not vintage")