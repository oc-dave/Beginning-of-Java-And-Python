# Create a list of strings called `my_list`
my_list = ['Python', 'Django', 'Java', 'Python', 'Ruby', 'Anaconda']

# Define a function called `check_for_Duplicates` that takes the list as an argument
def check_for_Duplicates(my_list):
    # Check if the list has any duplicates by comparing the length of the original list to the length of the set of the original list

    if len(my_list) == len(set(my_list)):
        # If the two lengths are the same, the list has no duplicates, so return `False`
        return False
    else:
        # If the two lengths are not the same, the list has duplicates, so return `True`
        return True


# Create a variable called result and store the 'check_for_duplicates' function in the 'result' variable
result = check_for_Duplicates(my_list)

# If 'result' is 'True', print 'Yes, list contains duplicates', else print 'No duplicates found in list'
if result is True:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')
