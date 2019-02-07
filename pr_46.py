# coding=utf-8
import random
from collections import Counter

def listofrandomnum (number, a, b):
    list =[]
    for i in range(number):
        randnum=random.randint(a,b)
        list.append(randnum)
    return list
cisla = listofrandomnum(100,10,120)



"""První možnost"""

def Repeat(x):
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

def repeat2 (cisla):
    usporadano =list(set(cisla))

    c1 = Counter(cisla)
    c2 = Counter(usporadano)
    diff = c1-c2
    vysledek = (list(diff.elements()))


    pocet= len(vysledek)
    print ("Počet duplicit je:",pocet)
    return (vysledek)

print (repeat2(cisla))

