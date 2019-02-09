# coding=utf-8

"""
Závěrečný úkol pro předmět: Úvod do Programování.
Zadání úkolu: Odstranění duplicitních prvků z posloupnosti a sdělení jejich počtu.
Vypracovala: Kristýna Měchurová, rok: 2019
"""

import random
from collections import Counter


def listofrandomnum (number, a, b):
    """ Vytvoří list náhodných celých čísel.
        Vstup:  number - počet čísel v řetězci
                a, b  - interval náhodných čísel
                (a: minimální hodnota intervalu
                 b: maximální hodnota intervalu)
        Výstup: list náhodných čísel."""

    list =[]
    for i in range(number):
        randnum=random.randint(a,b)
        list.append(randnum)
    return list

cisla = listofrandomnum(30,-5,10)

def listofint (listofnum):
    """Ošetření list obsahuje pouze celá čísla
      Vstup: list
      Výstup: list obsahující pouze celá čísla"""

    if all(isinstance(i, int) for i in listofnum)==True:
        return listofnum
    else:
        print ("List neobsahuje pouze celá čísla")
        quit (1)


"""První možnost"""

def Repeat(x):

    """Nalezne a vypíše duplicity a jejich počet
        Vstup: x - list celých čísel
        Výstup: list duplicitních hodnot, počet dupl. hodnot"""

    x=listofint(x)

    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j]and x[i] not in repeated:
                repeated.append(x[i])
    duplicity = []
    for i in x:
        if i in repeated:
            duplicity.append(i)
    print(duplicity)
    pocet=len(duplicity)-len(repeated)
    print("Počet duplicit:", pocet)
    return repeated

print (Repeat(cisla))



"""Druhá možnost"""

def repeat2 (numbers):
    """Nalezne a vypíše duplicity a jejich počet
        Vstup: numbers - list celých čísel
        Výstup: list duplicitních hodnot, počet dupl. hodnot"""


    numbers= listofint(numbers)
    sorted = list(set(numbers))
    c1 = Counter(numbers)
    c2 = Counter(sorted)
    diff = c1-c2
    vysledek = (list(diff.elements()))

    pocet= len(vysledek)
    print ("Počet duplicit je:",pocet)
    return (vysledek)


print (repeat2(cisla))

