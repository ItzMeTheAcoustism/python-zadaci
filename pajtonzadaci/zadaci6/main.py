brojac = 0

n = int(input("Unesi broj: "))
for i in range(n):
    broj = int(input("Unesi broj: "))
    if broj >= 15 and broj <= 55:
       brojac = brojac + 1

print(brojac)
