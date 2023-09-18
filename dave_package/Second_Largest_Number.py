def count_digit(string, digit):
    count = 0
    for char in string:
        if char == digit:
            count += 1
    return count


string = "dfa12321afd"
digit = '2'

result = count_digit(string, digit)
print(result)
