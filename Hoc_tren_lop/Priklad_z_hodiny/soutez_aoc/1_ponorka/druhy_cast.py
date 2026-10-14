from os.path import join, realpath, dirname
path = join(dirname(realpath(__file__)), "navigace.txt") 

horizontal =0
depth = 0
aim =0


with open (path,'r',encoding="utf-8") as f:
    for line in f :
        line = line.strip()
        direction, value = line.split()
        value = int(value)
        if direction == "forward":
            horizontal += value
            depth+= aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim-= value
print(f"horizontal: {horizontal}* depth: {depth} = {horizontal*depth}")


