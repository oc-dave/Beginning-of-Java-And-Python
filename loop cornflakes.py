school_name = "Aso Rock Secondary School, Abuja Nigeria"
class_name = "SSS 3"
total_students = 20
total_score = 0

print("School:", school_name)
print("Class:", class_name)
print("Number of Students in class:", total_students)

# Collect scores for each student
for i in range(1, 21):
    while True:
        score = int(input(f"Enter the score for student {i} out of 20: "))
        total_score += score
        if score < 0 or score > 100:
            print("Invalid score! Please enter a score between 0 and 100.")
        elif ValueError:
            break

# Compute the average score
    average_score = total_score / total_students

# Print the results
print("""
*****************************************************
School Name: {school_name}
*****************************************************
Class Name: {class_name}

Number of Students in class: {total_students}

Average Score: {average_score}

Total Score: {total_score}
*****************************************************
""")













