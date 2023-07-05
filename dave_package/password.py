password = int(input("Enter your 5 digit password : "))
print('Password saved.')
counter = 6

while counter > 0:
    user_entry = int(input('Enter Password: '))
    if user_entry == password:
        print("correct")

    if user_entry > 0 < 5:
        print(f"Your password is too short!,You have {counter} tries left")
    elif user_entry < 5:
        print(f"Your password is too long!,You have {counter} tries left")
        counter = counter-1