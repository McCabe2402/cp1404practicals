"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import  Car

class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${Taxi.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return Taxi.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        # Check if there is enough fuel
        fuel_needed = distance * 0.1  # Assuming the taxi consumes 0.1 fuel per km
        if self.fuel < fuel_needed:
            distance_driven = self.fuel / 0.1  # Drive only as far as the remaining fuel allows
            self.fuel = 0
            print(f"Not enough fuel. Can only drive {distance_driven} km.")
        else:
            distance_driven = distance
            self.fuel -= fuel_needed

        self.current_fare_distance += distance_driven
        return distance_driven




