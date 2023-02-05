#a. Írj egy függvényt (beker() néven), ami a minta alapján alkalmas három negatív egész szám bekérésére! (2p)

#b. Ha a felhasználó nem jó adatot adott meg, kérd be újra, míg jót nem ad meg! (1p)

#c. A program az adatbekérés után megkeresi,
#hogy a három beolvasott valós szám négyzete közül melyik a legkisebb,
#és hányadikként adta meg a felhasználó! A döntés eredményét a program írja ki a konzolra, a minta alapján! (4p)

def beker(i):
    szam = int(input(f"\tAdd meg a(z) {i+1}. negatív számot: "))
    while szam >= 0:
        szam = int(input(f"\tAdd meg újra a(z) {i+1}. NEGATÍV számot! "))
    return szam

def harom_beker():
    i = 0
    lista = []
    while i < 3:
        szam = beker(i)
        lista.append(szam)
        i += 1
    return lista

def legkisebb(lista):
    i = 0
    legkisebb = 0
    while i < len(lista):
        if lista[legkisebb] ** 2 > lista[i] ** 2:
            legkisebb = i
        i += 1
    print("I/c:")
    print(f"\tA legkisebb négyzetű szám: {lista[legkisebb]}, megadási sorrendje: {legkisebb+1}")
















