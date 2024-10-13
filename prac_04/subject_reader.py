"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_subject_details(data)


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

def display_subject_details(subjects):
    """Display the details of each student"""
    for subject in subjects:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")


main()