from guitar import Guitar

def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    current_year = 2024
    age1 = guitar1.get_age(current_year)
    age2 = guitar2.get_age(current_year)

    print(f"{guitar1.name} is {age1} years old")
    print(f"{guitar2.name} is {age2} years old")

    is_vintage1 = guitar1.is_vintage()
    is_vintage2 = guitar2.is_vintage()

    print(f"{guitar1.name} is vintage: {is_vintage1}")
    print(f"{guitar2.name} is vintage: {is_vintage2}")

if __name__ == "__main__":
    main()
