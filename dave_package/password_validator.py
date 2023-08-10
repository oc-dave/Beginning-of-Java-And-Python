def password_validator():
    while True:
        password = input("Enter your password: ")
        has_upper = any(a.isupper() for a in password)
        has_lower = any(a.islower() for a in password)
        has_digit = any(a.isdigit() for a in password)
        is_valid = len(password) >= 8 and has_upper and has_lower and has_digit

        if is_valid:
            return password
        errors = []
        if not has_upper:
            errors.append("Password should have at least one upper case letter. ")
        if not has_lower:
            errors.append("Password should have at least one lower case letter. ")
        if not has_digit:
            errors.append("Password should have at least one digit. ")
        if len(password) < 8:
            errors.append("Password should have at least 8 characters. ")
            print("Invalid password. please fix the following errors: ")
        for error in errors:
            print(f"- {error}")

valid_password = password_validator()
print("Valid password :", valid_password)