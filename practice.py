first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
age = int(input("Enter your age: "))

if first_name == "":
    print("You can't leave your first name blank!")

elif last_name == "":
    print("You can't leave your last name blank!")

elif age < 0:
    print("You can't enter a negative value")

elif age < 18:
    print(f"Your name is {first_name} {last_name}, your age is {age} and you're under aged")

elif age >= 65:
    print(f"Your name is {first_name} {last_name}, your age is {age} and you're old")

elif age > 18 <= 65:
    print(f"Your name is {first_name} {last_name}, your age is {age} and you're a citizen")







