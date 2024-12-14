best = 1.0
worst = 5.0

num_of_students = int(input("How many students? "))
for i in range(num_of_students):
    sum_of_grades = 0
    for i in range(5):
        grades = int(input("Input the students grades: "))
        sum_of_grades = sum_of_grades + grades
    average = sum_of_grades / 5
    print(average)
    if average > best:
        best = average
    elif average < worst:
        worst = average
    
print("The best average is", best, "and the worst is", worst)