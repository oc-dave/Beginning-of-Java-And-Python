import re


def email_validator(email):
    pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+'
    return bool(re.match(pattern, email))


Email = input('Enter your email addresses : ')
if email_validator(Email):
    print('Valid Email Address')
else:
    print('Invalid Email Address')
