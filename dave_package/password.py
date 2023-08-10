count = 10
counter = 6
Password = ''

while counter > 0:
    user_entry = str(input('Enter your Password: '))
    if user_entry == Password:
        print("Password Correct!")
        break
    elif len(user_entry) < 8:
        print(f"Your password is too short! You have {counter - 1} tries left.")
    elif len(user_entry) > 8:
        print(f"Your password is too long! You have {counter - 1} tries left.")
    else:
        print(f"Wrong password, Try again! {counter - 1} tries left")
    counter -= 1

if counter == 0:
    print("Sorry, you have reached the maximum number of tries.")
