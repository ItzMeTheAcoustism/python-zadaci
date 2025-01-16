elements = {
    "H" : 1.01,
    "Li" : 6.94,
    "Be" : 9.01,
    "He" : 4,
    "B" : 10.81,
    "C" : 12.01,
    "N" : 14.01,
    "O" : 16,
    "F" : 19,
    "Ne" : 20.18
}

pick_an_element = input("Chose an element from the first 2 groups of the periodic table: ")
print("Its atomic mass is", elements[pick_an_element])
