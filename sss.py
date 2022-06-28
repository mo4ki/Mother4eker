from time import sleep as sl
import random

i=0

math = random.randint(1, 3)

while i<=100:
    i = i + random.randint(1,12)
    print(f"Чекаем твою мать... ({str(i)}%)")
    sl(0.5)

if math == 1: print(data[0].translate(crypt(typ="dec")))
elif math == 2: print(data[1].translate(crypt(typ="dec")))
else: print(data[2].translate(crypt(typ="dec")))

input()
