import re


def vowel():
    if re.search(r'[aeiou]', letter):
        return bool


letter = input('Enter the letter : ')
if vowel():
    print('true')
else:
    print('false')

