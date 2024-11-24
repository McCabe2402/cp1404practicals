import random
from car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = random.randint(0, 100)
        if chance < self.reliability:
            super().drive(distance)
        else:
            print(f"The {self.name} failed to start due to its reliability.")