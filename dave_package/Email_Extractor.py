import re

text = input('Enter Text: ')
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}\b'

# Find and extract email addresses
emails = re.findall(pattern, text)

# Clean and format the extracted emails
cleaned_emails = ', '.join(emails)

print(f'Valid Emails: {cleaned_emails}')
