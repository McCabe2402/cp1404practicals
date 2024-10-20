COLOUR_HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    colour_name = input("Enter a color name (or leave blank to quit): ").strip().lower()

    while colour_name != "":
        if colour_name in COLOUR_HEX_CODES:
            hex_code = COLOUR_HEX_CODES[colour_name]
            print(f"The hexadecimal code for {colour_name.capitalize()} is {hex_code}")
        else:
            print(f"'{colour_name}' is not a valid hex code")
            colour_name = input("Enter a color name (or leave blank to quit): ").strip().lower()

    print("Goodbye!")


if __name__ == "__main__":
    main()
