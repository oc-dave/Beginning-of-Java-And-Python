import re


def odd_number():
    if re.search(r'[1, 5, 8, 3]', number):
        return bool


number = input('Enter a number: ')
if odd_number():
    print('true')
else:
    print('false')
