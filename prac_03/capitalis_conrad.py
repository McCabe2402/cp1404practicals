import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00  # Minimum price set to $1
MAX_PRICE = 100.00  # Maximum price set to $100
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
number_of_days = 0  # Initialize the day counter

print(f"Starting price: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment day counter
    price_change = 0

    # Randomly decide whether to increase or decrease the price
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)  # Update the price
    print(f"On day {number_of_days} price is: ${price:,.2f}")
