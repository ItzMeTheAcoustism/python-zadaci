try:
    age = float(input("Enter age(in years): "))
    if age >= 0 and age < 18:
        print("Cant drink yet")
    elif age > 18 and age < 100:
        print("No more tax evasion")
    else:
        print("Liar")
except:
    print("Nuh uh")




