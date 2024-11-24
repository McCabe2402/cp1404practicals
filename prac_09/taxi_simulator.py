from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0
    continue_trip = 'y'  # Initialize the flag to start the loop

    while continue_trip == 'y':
        current_taxi = choose_taxi(taxis, current_taxi)
        fare = drive_taxi(current_taxi)
        total_bill += fare

        print(f"Your total bill is: ${total_bill:.2f}")

        continue_trip = input("Do you want to continue driving? (y/n): ").lower()

    print(f"Final total bill: ${total_bill:.2f}")


def choose_taxi(taxis, current_taxi):
    print("Available taxis:")
    for i, taxi in enumerate(taxis, start=1):
        print(f"{i}. {taxi}")

    if current_taxi is None:
        choice = int(input("Please choose a taxi by number: "))
        current_taxi = taxis[choice - 1]
    return current_taxi


def drive_taxi(current_taxi):
    if current_taxi is None:
        print("You must choose a taxi before driving!")
        return 0

    distance = float(input("How far would you like to drive? "))
    distance_driven = current_taxi.drive(distance)
    fare = current_taxi.get_fare()

    print(f"Driven {distance_driven} km.")
    print(f"Fare for the trip: ${fare:.2f}")
    return fare


main()