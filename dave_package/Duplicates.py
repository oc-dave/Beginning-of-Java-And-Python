my_list = [2, 2, 1, 1, 4, 3, 3, 5, 5, 5]
unique_digits = [i for i in my_list if my_list.count(i) == 3]
result = unique_digits[0] if unique_digits else my_list
print(result)
