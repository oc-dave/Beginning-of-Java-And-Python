counter = 0
student_pass = 0
fail = 0
while counter <= 10:
    grade = int(input("Enter 1 for pass and 2 for fail: "))

    if grade == 1:
        student_pass = student_pass + 1

    else:
        fail = fail + 1

    counter = counter + 1

    if student_pass > 8:
        print("Bonus to the teacher...")
        