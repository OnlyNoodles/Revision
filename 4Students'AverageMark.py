def number_checker(question):
    error = "\nPlease enter a valid number.\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


highest_grade = 0
highest_grade_student = ""

while True:
    students_name = input("Enter the name of the student.\n"
                          "To exit, enter 'X'.\nType here: ")
    if students_name == "X":
        break
    else:
        students_grade = number_checker(f"Enter {students_name}'s mark: ")
        if students_grade > highest_grade:
            highest_grade = students_grade
            highest_grade_student = students_name

print(f"The highest mark is {highest_grade} from {highest_grade_student}")
