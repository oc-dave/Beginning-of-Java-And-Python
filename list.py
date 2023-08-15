numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers[::2])
print(total)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers[1::2])
print(total)

numbers = [10, 20, 30, 40, 50]
squares = []
total = 0

for x in numbers:
    square = x ** 2
    squares.append(square)
    total += square

print("Squared numbers:", squares)
print("Sum of squared numbers:", total)

numbers = [10, 20, 30, 40, 50]
total = 0

for x in numbers:
    total += x

print(total)

numbers = [10, 20, 30, 40, 50]
total = 0

for x in numbers[0::2]:
    total += x

print(total)

numbers = [10, 20, 30, 40, 50]
total = 0

for x in numbers[1::2]:

    total += x

print(total)

numbers = [10, 20, 30, 40, 50]
squares = []
total = 0

for x in numbers:
    square = x ** 2
    squares.append(square)
    total += square

print("Squared numbers:", squares)
print("Sum of squared numbers:", total)
