def findTopGrades(num_of_students):
    grade_counter = 0
    for i in range(num_of_students):
        grade = int(input("Input student grade: "))
        if grade == 5:
            grade_counter = grade_counter + 1
    return grade_counter