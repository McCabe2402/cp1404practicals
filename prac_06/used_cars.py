"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class with named cars."""

    # Create the first car object
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(my_car)  # Print my_car to check __str__ output

    # Create a limo car object
    limo = Car("Limo", 100)
    print(limo)  # Print limo to check __str__ output

    # Add fuel to limo and check
    limo.add_fuel(20)
    print(limo)  # Print limo to check updated fuel

    # Drive the limo and check its state
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km and now has {limo.fuel} units of fuel remaining.")
    print(limo)  # Print limo to check final state


main()

