import math

num = int(input("Enter a number: "))


def divide_or_square(num):
    if num % 5 == 0:
        return math.sqrt(num)
    else:
        return num % 5


print(divide_or_square(num))
