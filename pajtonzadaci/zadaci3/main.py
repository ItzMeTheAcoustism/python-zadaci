from pravogaonik import Pravogaonik

class Aplikacija:
    def __init__(self):
        pass
    def main(self):
        a = int(input("Stranica a = "))
        d = int(input("Dijagonala d = "))
        object = Pravogaonik(a,d)
        print("Stranica b je ", object.izracunaj_b())


aplikacija = Aplikacija()
aplikacija.main()