guitar = "Gibson L-5 CES"
year = 1922
price = 16036.0

formatted_string = f"{year} {guitar} for about ${price:,.2f}!"
print(formatted_string)

for i in range(11):
    result = 2 ** i
    print(f"2 ^ {i:>2} is {result:>4}")