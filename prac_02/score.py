"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
# Changed to format both possible out of bounds.
if score < 0 or score > 100:
    print("Invalid score")
else:
    # Removed if, if, if and reformatted to if, elif, else
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    # Changed Bad to Fail.
    else:
        print("Fail")
