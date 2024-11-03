class Guitar:
    def __init__(self, name, year, cost):
        """Initialize a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar instance."""
        return f"My guitar: {self.name}, first made in {self.year}, costs ${self.cost:,.2f}"


if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)