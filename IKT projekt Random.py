import random
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
        try:
            n = int(input("Hány számot akar generálni: "))
        except ValueError as hiba:
            print(f"'{hiba}' nem megfelelő paraméter!")
            Option1()
        try:
            felsoH = int(input("Generált számok felső határa: "))
        except ValueError as hiba:
            print(f"'{hiba}' nem megfelelő paraméter!")
            Option1()
        try:
            alsoH = int(input("Generált számok alsó határa: "))
        except ValueError as hiba:
            print(f"'{hiba}' nem megfelelő paraméter!")
            Option1()
        f = open("ki.txt", "w")
        for x in range(n):
            r = random.randint(alsoH, felsoH)
            f.write(f"{r};")
        f.close
def Option2():
        try:
            n = int(input("Hány szöveget akar generálni: "))
        except ValueError as hiba:
            print(f"'{hiba}' nem megfelelő paraméter!")
            Option2()
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
            try:
                n = int(input("Hány számot akar generálni: "))
            except ValueError as hiba:
                print(f"'{hiba}' nem megfelelő paraméter!")
                Option3()
            try:
                felsoH = int(input("Generált számok felső határa: "))
            except ValueError as hiba:
                print(f"'{hiba}' nem megfelelő paraméter!")
                Option3()
            try:
                alsoH = int(input("Generált számok alsó határa: "))
            except ValueError as hiba:
                print(f"'{hiba}' nem megfelelő paraméter!")
                Option3()
            with open("ki.txt", "r") as f:
                numbers = f.read().split(";")
            del numbers[-1] #az utolsó elem egy üres ''
            numbers = [eval(i) for i in numbers]
            if n == len(numbers):
                for x in range(len(numbers)):
                    if numbers[x-1] >= alsoH and numbers[x-1] <= felsoH:
                        None
                    else:
                        print("A lista nem felel meg a paramétereknek!")
                        Start()
                print("A lista megfelel a paramétereknek!")
            else:
                print("A lista nem felel meg a paramétereknek!")
                Start()
def Option4():
        try:
            f = open("ki.txt")
        except FileNotFoundError:
            print("Generáljon először fájlt a 2. opció segítségével!")
            Start()
        else:
            try:
                n = int(input("Generált szövegek száma: "))
            except ValueError as hiba:
                print(f"'{hiba}' nem megfelelő paraméter!")
                Option4()
            Charachters = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","J","j","K","k","L","l","M","m","N","n","O","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
            with open("ki.txt", "r") as f:
                szöveg = f.read().split(";")
            del szöveg[-1] #az utolsó elem egy üres ''
            if n == len(szöveg):
                print(szöveg)
                for x in range(len(szöveg)):
                    for i in range(len(szöveg[x])):
                        if szöveg[x][i] in Charachters:
                             None
                        else:
                            print("A lista nem felel meg a paramétereknek!")
                            Start()
                print("A lista megfelel a paramétereknek!")
            else:
                print("A lista nem felel meg a paramétereknek!")
                Start()
Start() #Program kezdése :D