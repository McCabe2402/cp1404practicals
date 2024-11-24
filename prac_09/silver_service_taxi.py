from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        base_str = super().__str__().replace("odometer", "odo")
        return (f"{base_str}, {self.current_fare_distance}km on current fare,"
                f" ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}")

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + self.flagfall
