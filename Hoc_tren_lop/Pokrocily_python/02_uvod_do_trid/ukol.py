class Kniha:
    def __init__(self,nazev:str,autor:str,pocet_stran:int):
        self.nazev = nazev
        self.autor = autor
        self.pocet_stran = pocet_stran
    def info(self)->None: # de ko tra ve None
        return f"Kniha {self.nazev}, autor {self.autor}, pocet {self.pocet_stran}"

kniha1 = Kniha("No Home","Hector Marlot",650)
print(kniha1.info())
