class Pes:
    def __init__(self,jmeno,rasa):
        self.jmeno = jmeno
        self.rasa = rasa

    def stekej(self):
        print(f"{self.jmeno}: half half")

pes1 = Pes("Moon","rasa")
print(pes1.stekej())
