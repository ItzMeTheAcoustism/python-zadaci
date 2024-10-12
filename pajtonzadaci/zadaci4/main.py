n = int(input("Unesi broj: "))

if n <= 10:
    for i in range(n):
        print("I bet you chose a number between 0-10, didnt you?")
else:
    for i in range(n):
        print("I bet you chose a number over 10, didnt you?")