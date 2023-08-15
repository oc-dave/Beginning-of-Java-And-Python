color_list = ['RED', 'GREEN', 'WHITE', 'BLACK']


def sorted_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
            return lst[1::2]


print(sorted_list(color_list))
