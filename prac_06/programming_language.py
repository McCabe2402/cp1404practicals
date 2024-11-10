"""
Subject: CP1404
Name of file: programming_language.py
Estimate time taken: 10 mins
Actual time taken: 10 mins

"""

class ProgrammingLanguage:
    """Represents a programming language with its typing, reflection, and creation year"""
    def __init__(self, name, typing, reflection, year):
        """Initializes the programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string representation of the programming language"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Checks if the programming language is dynamically typed"""
        return self.typing.lower() == "Dynamic"