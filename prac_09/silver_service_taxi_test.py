from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    fancy_taxi = SilverServiceTaxi("Luxury Taxi", 100, 2)
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    expected_str = "Luxury Taxi, fuel=82, odo=18, 18km on current fare, $2.46/km plus flagfall of $4.50"
    expected_fare = 18 * 2.46 + 4.50

    print(f"Expected Fare: ${expected_fare:.2f}")
    print(f"Actual Fare: ${fancy_taxi.get_fare():.2f}")
    print(f"Expected String: {expected_str}")
    print(f"Actual String: {str(fancy_taxi)}")

    assert fancy_taxi.get_fare() == expected_fare


test_silver_service_taxi()
