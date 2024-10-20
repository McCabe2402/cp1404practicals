import csv
from collections import defaultdict

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def get_records(filename):
    """Read the CSV file and return the records as a list"""
    records = []
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            records.append(row)
    return records

def process_records(records):
    """Process the records and return the records as a list"""
    champion_to_count = defaultdict(int)
    countries = set()

    for record in records:
        champion = record[INDEX_CHAMPION]
        country = record[INDEX_COUNTRY]

        champion_to_count[champion] += 1
        countries.add(country)

    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display the results of champions and countries"""
    print("Champions and Their Win Counts")
    for champion, count in champion_to_count.items():
        print(f"{champion}: {count} times")

    sorted_countries = sorted(countries)
    print("\nCountries of the Champions (Alphabetical Order)")
    for country in sorted_countries:
        print(country)

if __name__ == '__main__':
    main()