"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(",") # Remove the \n
        parts[2] = int(parts[2]) # Make the number an integer
        data.append(parts) #Append the parts for the data list
    input_file.close()
    return data # Return the nested list


main()