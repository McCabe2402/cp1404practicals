COLOR_HEX_CODES = {
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
    color_name = input("Enter a color name (or leave blank to quit): ").strip().lower()

    while color_name != "":
        hex_code = COLOR_HEX_CODES[color_name]

        if hex_code:
            print(f"The hexadecimal code for {color_name.capitalize()} is {hex_code}")
        else:
            print(f"'{color_name}' is not a valid hex code")

        color_name = input("Enter a color name (or leave blank to quit): ").strip().lower()

    print("Goodbye!")


if __name__ == "__main__":
    main()
