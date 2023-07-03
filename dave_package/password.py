password = int(input("Enter your 8 digit password : "))
print('Password saved.')
tries = 6

for x in range(1, 7):
    while tries > 0:
        print('Enter Password: ')
    if password < 8:
        retry = int(input(f"You have {tries} tries left"))
        print("Your password is too short")
    else:
        password > 8
        print("Your password is too long")
    if password == password:
        print("Password correct!")
        break
    if tries == 0:
        print("Sorry, you ran out of tries.")

tries -= 1


