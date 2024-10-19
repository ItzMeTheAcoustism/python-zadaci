n = int(input("Unesi broj takmičara: "))

maks = 0

for i in range(n):
    skok = float (input("Unesi skok u dalj: "))
    if skok > maks:
        maks = skok

print(maks)