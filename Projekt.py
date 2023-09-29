szamok="0123456789"
betuk="ABCDEFGHIJKLMNOPQRSTUVWXYZaeioubcdfghjklmnprstvz"
adatok=[]
with open("ki.txt", "r", encoding="utf-8") as file:
    adatok = file.read().split(";")
del adatok[-1]

if not all(x in szamok + betuk or ';' for x in adatok):
    print("Helytelen adatok.")
else:
    kerdes = input("Növekvő vagy csökkenő rendezés? (növekvő/csökkenő) ").lower()
    print("Buborékrendezés:")
    n = len(adatok)

    if kerdes == "növekvő":
        for i in range(n):
            for j in range(0, n-i-1):
                if adatok[j] > adatok[j+1]:
                    adatok[j], adatok[j+1] = adatok[j+1], adatok[j]
        if(x in szamok for x in adatok):
            print("Növekvő sorrendben rendezett számok: " + '; '.join(adatok))
        elif(x in betuk for x in adatok):
            print("Növekvő sorrendben rendezett betűk: " + '; '.join(adatok))
    elif kerdes == "csökkenő":
        for i in range(n):
            for j in range(0, n-i-1):
                if adatok[j] < adatok[j+1]:
                    adatok[j], adatok[j+1] = adatok[j+1], adatok[j]
        if(x in szamok for x in adatok):
            print("Növekvő sorrendben rendezett számok: " + '; '.join(adatok))
        elif(x in betuk for x in adatok):
            print("Növekvő sorrendben rendezett betűk: " + '; '.join(adatok))
    else:
        print("Hibás bevitel.")

    print("Összefésüléses rendezés: ")

    if kerdes == "növekvő":
        n = len(adatok)
        if n > 1:
            middle = n // 2
            left_half = adatok[:middle]
            right_half = adatok[middle:]

            left_half.sort()
            right_half.sort()

            i, j, k = 0, 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    adatok[k] = left_half[i]
                    i += 1
                else:
                    adatok[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                adatok[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                adatok[k] = right_half[j]
                j += 1
                k += 1
        if(x in szamok for x in adatok):
            print("Növekvő sorrendben rendezett számok: " + '; '.join(adatok))
        elif(x in betuk for x in adatok):
            print("Növekvő sorrendben rendezett betűk: " + '; '.join(adatok))
    elif kerdes == "csökkenő":
        n = len(adatok)
        if n > 1:
            middle = n // 2
            left_half = adatok[:middle]
            right_half = adatok[middle:]

            left_half.sort(reverse=True)
            right_half.sort(reverse=True)

            i, j, k = 0, 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] > right_half[j]:
                    adatok[k] = left_half[i]
                    i += 1
                else:
                    adatok[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                adatok[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                adatok[k] = right_half[j]
                j += 1
                k += 1
        if(x in szamok for x in adatok):
            print("Növekvő sorrendben rendezett számok: " + '; '.join(adatok))
        elif(x in betuk for x in adatok):
            print("Növekvő sorrendben rendezett betűk: " + '; '.join(adatok))
    else:
        print("Hibás bevitel.")

    while True:
        uj_elem = input("Adjon meg egy új számot, vagy nyomjon egy entert a kilépéshez: ")

        if not uj_elem:  
            break

        if kerdes == "növekvő":
            for i, elem in enumerate(adatok):
                if uj_elem < elem:
                    adatok.insert(i, uj_elem)
                    break
            else:
                adatok.append(uj_elem)
                break
        elif kerdes == "csökkenő":
            for i, elem in enumerate(adatok):
                if uj_elem > elem:
                    adatok.insert(i, uj_elem)
                    break
            else:
                adatok.append(uj_elem)
                break

    print("Az új rendezett lista: " + '; '.join(adatok))
