age = int(input("Input age: "))
fitness_goal = input("Whats your fitness goal? Losing weight, Building muscle or staying active? ")
injury = input("Do you have any sort of injury? ")

if age <= 16 and injury == "no" and fitness_goal == "losing weight":
    print("Light activity like walking or yoga is best at your age.")
if injury == "yes":
    print("Consult a physiotherapist before starting any workout.")
if age < 40 and age > 16 and fitness_goal == "losing weight" and injury == "no":
    print("Try cardio workouts like running or HIIT.")
if fitness_goal == "building muscle" or fitness_goal == "build muscle" and age < 60 and injury == "no":
    print("Focus on strength training with weights.")
if fitness_goal == "staying active" and age < 60 and injury == "no":
    print("30 minutes of daily movements like cycling or dancing is great!")
if age >= 60 and fitness_goal == "staying active" and injury == "no":
    print("Low impact exercises like swimming and streches are best for seniors.")

if fitness_goal != "losing weight" and fitness_goal != "building muscle" and fitness_goal != "staying active":
    print("Invalid fitness goal entered, read the instructions and try again.")
