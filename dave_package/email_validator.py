import re


def email_validator(email):
    if re.search(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+', Email):
        return bool(email)


Email = input('Enter your email addresses : ')
if email_validator(Email):
    print('Valid Email Address')
else:
    print('Invalid Email Address')
