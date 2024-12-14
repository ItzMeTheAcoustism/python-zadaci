students_n_grades = {
    "Mabel": [3, 3, 2, 4, 5],
    "Bill": [5, 5, 5, 5, 5],
    "Stanford": [5, 5, 5, 5, 2],
    "Mason": [5, 5, 4, 4, 3],
    "Stanley": [4, 3, 3, 2, 5],
    "Fiddleford": [5, 5, 4, 5, 5]
}

best = 1.0
best_student = ""
worst = 5.0
worst_student = ""

for name in students_n_grades:
    sum_of_grades = sum(students_n_grades[name])
    num_of_grades = len(students_n_grades[name])
    average = sum_of_grades / num_of_grades
    if average > best:
        best = average
        best_student = name
    elif average < worst:
        worst = average
        worst_student = name

print("The best student is", best_student, "with an average of", best, ", the worst student is", worst_student, "with an average of", worst)
