grades_list = []
grade = 0

while True:
    grade = int(input("Input grade: "))
    
    if grade == 0:
        break
    else:
        grades_list.append(grade)

final_grade = lambda grades_list: sum(grades_list) / len(grades_list)
print(final_grade(grades_list))