# coding=utf-8
import sys, os
import random

list =[]
for i in range(20):
    nahodnecisla=random.randint (100,110)
    list.append(nahodnecisla)

print (list)


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

repeated= (Repeat(list))

print (repeated)

