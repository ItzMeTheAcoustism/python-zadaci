import random

first_five = random.sample(range(1, 35), 5)

last_num = random.sample(range(1, 10), 1)
last_num = last_num[0]
print(first_five[0])
print(last_num)

first, second, third, fourth, fifth, sixth = map(int, input("Pick 5 numbers(1-35) and then one more number(1-10): ").split())

counter = 0
score = False
for i in range(len(first_five)):
    if first_five[1] == first or first_five[2] == second or first_five[3] == third or first_five[4] == fourth or first_five[5] == fifth:
        counter = counter + 1

if sixth == last_num:
    score = True

if score == True:
    print("You have guessed", counter + 1)
else:
    print("You have guessed", counter + 0)