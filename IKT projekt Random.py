import random
import os

def Start():
    print("1.Egész számok generálása")
    print("2.Betűk generálása")
    print("3.ki.txt elenőrzése számokkal")
    print("4.ki.txt ellenőrzése betűkkel")
    print("Írja be a választott opció számát: ")
    UserInput = input()

    if UserInput == "1":
        Option1()

    elif UserInput == "2":
        Option2()

    elif UserInput == "3":
        Option3()

    elif UserInput == "4":
        Option4()
    else:
        print("Nincs ilyen opcio :c") 
        Start()
    
def Option1():
        n = int(input("Hány számot akar generálni: "))
        felsoH = int(input("Generált számok felső határa: "))
        alsoH = int(input("Generált számok alsó határa: "))
        f = open("ki.txt", "w")
        for x in range(n):
            r = random.randint(alsoH, felsoH)
            f.write(f"{r};")
        f.close
def Option2():
        n = int(input("Hány szöveget akar generálni: "))
        f = open("ki.txt", "w")
        Charachters = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","O","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
        for x in range(n):
            lenght = random.randint(1,20)
            for x in range(lenght):
                character = random.randint(0, 41)
                f.write(Charachters[character])
            f.write(";")
def Option3():
        try:
            f = open("ki.txt")
        except FileNotFoundError:
            print("Generáljon először fájlt az 1. opció segítségével!")
            Start()
        else:
            n = int(input("Hány számot akar generálni: "))
            felsoH = int(input("Generált számok felső határa: "))
            alsoH = int(input("Generált számok alsó határa: "))

def Option4():
        print("Option4")
        input()
Start()