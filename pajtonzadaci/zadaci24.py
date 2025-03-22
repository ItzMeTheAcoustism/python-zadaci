def finalGrade(**kwargs):
    final_grade = 0
    sum_of_grades = 0
    for key in kwargs:
        sum_of_grades = sum_of_grades + kwargs[key]
    final_grade = sum_of_grades / len(kwargs)
    return round(final_grade, 2)

print(finalGrade(grade1 = 5, grade2 = 2, grade3 = 4, grade4 = 5, grade5 = 1, grade6 = 5))
        
