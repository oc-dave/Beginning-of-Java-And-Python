def print_full_name(first_name, last_name):
    first_name = f'{first_name}'
    last_name = f'{last_name}'
    if len(first_name and last_name) > 10:
        print('Name too long')
    else:
        print("")


first = input('Enter your first name: ')
last = input('Enter your last name: ')
print_full_name(first, last)
print(f"{f'{first} {last}'}"",You just delved your into python!")
