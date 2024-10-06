is_finished = False
result = None  # Initialize result to None to handle undefined case

while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True to exit the loop
    except ValueError:  # Catch ValueError specifically for invalid integer conversion
        print("Please enter a valid integer.")

if result is not None:  # Check if result is defined before printing
    print("Valid result is:", result)
