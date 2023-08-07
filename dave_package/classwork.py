import math

num = int(input("Enter a number: "))


def divide_or_square(num):
    return math.sqrt(num) if num % 5 == 0 else num % 5


print(divide_or_square(num))
