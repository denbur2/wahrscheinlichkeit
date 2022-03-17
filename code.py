import random
import time
import os

from numpy import sort


würfelcounter = 0
ratecounter = 0
ratecounter2 = 0
register = [[1, 0],[2, 0],[3, 0],[4, 0],[5, 0],[6, 0]]

while True:
    würfelcounter += 1

    gewürfelt = random.randint(1, 6)
    for i in range(7):
        if gewürfelt == i:
            register[i-1][1] = register[i-1][1]+1



    #raten
    geraten = random.randint(1, 6)
    if geraten == gewürfelt:
        ratecounter += 1

    #raten2
    kurzregister = (sorted(register, key=lambda x:x[1]))
    if kurzregister[0][1] == gewürfelt:
        ratecounter2 += 1
    #mit wahrscheinlichkeit raten


    

    print("richtig geraten:", ratecounter, round((ratecounter/würfelcounter)*100, 3), "%")
    print("richtig berechnet:", ratecounter2, round((ratecounter2/würfelcounter)*100, 3), "%")
    print("würfelcounter:", würfelcounter)
    print("register: ",register)


    time.sleep(1)
    os.system('cls')