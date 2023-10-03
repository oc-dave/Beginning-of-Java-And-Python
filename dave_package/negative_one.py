def find_first_digit(string):
    for i, char in enumerate(string):
        if char.isdigit():
            return i
        else:
            return -1


input_string = "abcd1111"

result = find_first_digit(input_string)
print(result)
