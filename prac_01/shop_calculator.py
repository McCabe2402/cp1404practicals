# Get the number of items
number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Please enter a positive integer")
    number_of_items = int(input("Enter the number of items: "))
# Initialize total price
total_price = 0
# Loop through each item to get its price
for i in range(1, number_of_items + 1):
    price = float(input(f"Enter the price of item {i}: "))
    total_price += price
# Apply discount if total price exceeds $100
if total_price > 100:
    total_price *= 0.9
print(f"Total price: ${total_price:.2f}")