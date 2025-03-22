def sumNumbers(**kwargs):
    sum_result = 0
    for key in kwargs:
        sum_result = sum_result + kwargs[key]
    return sum_result


print(sumNumbers(num1 = 3, num2 = 4, num3 = 12, num4 = 10))
print(sumNumbers(num1 = 1, num2 = 5))
