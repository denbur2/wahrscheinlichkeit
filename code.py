import random
import time
import os


würfelcounter = 0
ratecounter = 0
register = [[0],[0],[0],[0],[0],[0]]

while True:
    würfelcounter += 1

    gewürfelt = random.randint(1, 6)
    for i in range(7):
        if gewürfelt == i:
            register[i-1][0] = register[i-1][0]+1



    #raten
    geraten = random.randint(1, 6)
    if geraten == gewürfelt:
        ratecounter += 1
    
    #mit wahrscheinlichkeit raten


    

    print("richtig geraten:", ratecounter,"\nwürfelcounter:", würfelcounter)
    print("register: ",register)


    time.sleep(1)
    os.system('cls')