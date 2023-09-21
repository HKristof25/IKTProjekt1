szamok=["1","2","3","4","5","6","7","8","9","0"]
betuk=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a", "e", "i", "o", "u", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
adatok=[]
with open("ki.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor)

for x in szamok:
    if x in adatok:
        kerdes=input("Növekvő vagy csökkenő rendezés? (növekvő/csökkenő) ")
        if kerdes=="növekvő":
            adatok.sort(reverse=False, key=None)
            print(adatok)
        elif kerdes=="csökkenő":
            adatok.sort(reverse=True, key=None)
            print(adatok)
        
        else:
            print("Hibás bevitel.")

for x in betuk:
    if x in adatok:
