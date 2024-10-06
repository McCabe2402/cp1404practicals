"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (must not be zero): "))
    while denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
        denominator = int(input("Enter the denominator (must not be zero): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


"""When will a valueerror occur?"""
# A ValueError will occur if the user inputs something that cannot be converted to an integer.
"""When will A zerodivisionerror occur"""
# When the user inputs 0 as the denominator.
"""Could you change the code to avoid the possibility of a zerodivisionerror"""
# Yes, you could change the code to avoid it by adding a check for the denominator before performing the division.

