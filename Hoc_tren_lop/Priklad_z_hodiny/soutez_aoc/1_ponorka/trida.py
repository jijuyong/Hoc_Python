from os.path import join, realpath, dirname

class Ponorka:
    def __init__(self):
        self.x:int=0
        self.y:int=0
        self.aim:int =0

    def zpracuj_prikaz(self,comman:tuple[str,int]):
        direction,value= comman
        if direction =="forward": self.x+=value
        elif direction =="up": self.y-=value
        elif direction =="down": self.y+=value
        else: pass

    def zpracuj_prikaz_2(self,comman:tuple[str,int]):
        direction , value = comman

        if direction == "forward":
            self.x += value
            self.y+= self.aim * value
        elif direction == "down":
            self.aim += value
        elif direction == "up":
            self.aim-= value
        else: pass


    def naviguj(self,navigacni_soubor:str,druha_cast):
        path = join(dirname(realpath(__file__)),navigacni_soubor)
        with open(path,'r',encoding="utf-8") as f:
            for line in f:
                command = (line.split()[0],int(line.split()[1]))
                if druha_cast ==True:
                    self.zpracuj_prikaz_2(command)
                else: self.zpracuj_prikaz(command)


    def __repr__(self):
        return f"{self.x};{self.y},vysledna vzdalenost: {self.x*self.y}"

if __name__ == "__main__":
    ponorka = Ponorka()



    ponorka.zpracuj_prikaz(("forward",10))
    ponorka.zpracuj_prikaz(("up",10))
    ponorka.zpracuj_prikaz(("down",10))

    print(ponorka.__repr__())