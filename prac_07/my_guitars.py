from guitar import Guitar, read_guitars_from_csv, display_guitars, add_new_guitar, write_guitars_to_csv


def main():
    file_name = "guitars.csv"
    guitars = read_guitars_from_csv(file_name)
    guitars.sort(key=lambda guitar: guitar.year)
    display_guitars(guitars)
    new_guitar = add_new_guitar()
    guitars.append(new_guitar)
    print("\nUpdated List of Guitars:")
    display_guitars(guitars)
    write_guitars_to_csv(file_name, guitars)


if __name__ == "__main__":
    main()
