#Example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#C
stars_number = int(input("How many stars?: "))
for i in range(stars_number):
    print('*', end=' ')
print()

#D
for i in range(1, stars_number + 1):
    print('*' * i)
print()
