count = 10
counter = 6
Password = ""

while count > 0:
    Password = str(input("Enter your 8 characters password: "))
    if len(Password) == 8:
        print("Password Saved")
        break
    else:
        print(f"You have {count - 1} tries to enter your 8 characters password ")
    count -= 1

    if count == 0:
        print("Sorry, you have reached the maximum number of entries.")
        break

while counter > 0:
    user_entry = str(input('Re-Enter your Password: '))
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
