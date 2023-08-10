print("Welcome to my RollerCoaster Ride!")
Height = int(input("Please Enter your Height: "))
if Height >= 6:
    print("You are allowed to Ride the RollerCoaster! ")

    Age = int(input("Please Enter your Age: "))
    if Age < 12:
        print("You are to pay N100 to ride ")
    elif 12 < Age <= 60:
        print("You are to pay N200")
    elif Age >= 60 or Age == 80:
        print("You are allowed to ride for free!!!")
    elif Age > 80:
        print("You are mad,go home!!")
else:
    print("You are not allowed to ride the RollerCoaster")