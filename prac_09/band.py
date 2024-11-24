class Band:
    """Band class for storing details of a band and its musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of the Band, showing its variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's musician collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing what each musician is playing."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
