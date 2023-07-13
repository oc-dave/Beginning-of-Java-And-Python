numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]


def sorted_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst


print(sorted_list(numbers))
print(sorted_list(numbers)[::-1])
