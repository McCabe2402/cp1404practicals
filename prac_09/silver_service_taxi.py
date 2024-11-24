from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi that includes fanciness and flagfall"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness