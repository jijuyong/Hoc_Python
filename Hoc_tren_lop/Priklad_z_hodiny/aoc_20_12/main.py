class Ship:
    def __init__(self):
        self.e =0
        self.w=0
        self.n=0
        self.s=0
        self.direction:str= 'E'
        self.stupnu = 90

    def rotace(self,seznam:list[str]):
        direction:str= ""
        value =0
        for i in seznam:
            direction = i[0]
            value = int(i[1:])
            if direction == 'N':
                self.n+=value
                self.direction = direction
            elif direction == 'S':
                self.s+=value
                self.direction = direction

            elif direction == 'E':
                self.e+=value
                self.direction = direction
            elif direction == 'W':
                self.w+=value
                self.direction = direction
            else: pass

            if direction == 'L':
                self.stupnu-=value
            elif direction == 'R':
                self.stupnu+= value
            elif direction == 'F':
                if self.direction == 'S':
                    self.s+=value
                elif self.direction == 'N':
                    self.n+=value
                elif self.direction == 'E':
                    self.e+=value
                elif self.direction =='W':
                    self.w+=value
                else: pass

            

        return [self.direction, (f"E:{self.e},W:{self.w},S:{self.s},N{self.n}")]




commands = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
    "S5",
    "E8",
    "W2"
]

ship1 = Ship()
toa_do_hien_tai = ship1.rotace(commands)
print(toa_do_hien_tai)
        
