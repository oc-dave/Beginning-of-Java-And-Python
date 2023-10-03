my_list = ['Python', 'Django', 'Java', 'Python', 'Ruby', 'Anaconda']


def check_for_Duplicates(my_list):
    return len(my_list) != len(set(my_list))


result = check_for_Duplicates(my_list)

if result is True:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')
