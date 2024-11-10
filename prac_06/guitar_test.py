from guitar import Guitar

def main():
    test_get_age()
    test_is_vintage()

def test_get_age():
    current_year = 2024
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    expected_age = current_year - 1922
    actual_age = guitar.get_age(current_year)
    print(f"{guitar.name} age test - Expected: {expected_age}. Got: {actual_age}")

def test_is_vintage():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00) # Not a guitar expert... sorry

    expected_vintage1 = True
    actual_vintage1 = guitar1.is_vintage()
    print(f"{guitar1.name} is_vintage() test - Expected: {expected_vintage1}. Got: {actual_vintage1}")

    expected_vintage2 = False
    actual_vintage2 = guitar2.is_vintage()
    print(f"{guitar2.name} is_vintage() test - Expected: {expected_vintage2}. Got: {actual_vintage2}")

if __name__ == "__main__":
    main()
