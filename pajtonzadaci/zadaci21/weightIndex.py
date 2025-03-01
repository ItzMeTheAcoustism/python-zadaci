def ideal_BMI(gender, height, weight):
    if gender == "f":          #female
        if height - 110 == weight:
            return "yes"
        else:
            return "no"
    if gender == "m":
        if height - 100 == weight:
            return "yes"
        else:
            return "no"