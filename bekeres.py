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
















