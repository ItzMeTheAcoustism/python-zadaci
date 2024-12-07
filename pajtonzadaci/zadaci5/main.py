from speed import Brzina

s1 = 15
t1 = 1
s2 = 12
t2 = 2.5
s3 = 6
t3 = 2

class Racunjanje_Brzina:
    def __init__(self, s, t):
        self.s = s
        self.t = t
    def brzine_zadate(self, s, t):
        object = Brzina(s1, t1)
        object = Brzina(s2, t2) 
        object = Brzina(s3, t3)

class Aplikacija:
    def __init__(self):
        pass
    def srednja_brzina(self, V1, V2, V3):
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
    def racunjanje_srednje_brzine(self, V1, V2, V3):
        return print("Srednja brzina je", (V1 + V2 + V3) / 3)
       


V1 = aplikacija = Racunjanje_Brzina(s1, s1)
V1 = aplikacija.brzine_zadate(s1, t1)
V2 = aplikacija = Racunjanje_Brzina(s2, t2)
V2 = aplikacija.brzine_zadate(s2, t2)
V2 = aplikacija = Racunjanje_Brzina(s3, t3)
V3 = aplikacija.brzine_zadate(s3, t3)
aplikacija = Aplikacija()
aplikacija.racunjanje_srednje_brzine(V1, V2, V3)
