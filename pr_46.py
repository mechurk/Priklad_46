# coding=utf-8

"""
Závěrečný úkol pro předmět: Úvod do Programování.
Zadání úkolu: Odstranění duplicitních prvků z posloupnosti a sdělení jejich počtu.
Vypracovala: Kristýna Měchurová, rok: 2019
"""

import random
import numpy as np
from collections import Counter
import sys


def fromtxttolist(text):
    """Z textového souboru vytvoří list
    Vstup: textový soubor
    Výstup: list celých čísel"""
    try:
        text_file = open(text, "r")
        lines = text_file.read().split(",")
        result = list(map(int, lines))
        print(result)
        text_file.close()
        return (result)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error")
        raise


def listofrandomnum(number, a, b):
    """ Vytvoří list náhodných celých čísel.
        Vstup:  number - počet čísel v řetězci
                a, b  - interval náhodných čísel
                (a: minimální hodnota intervalu
                 b: maximální hodnota intervalu)
        Výstup: list náhodných čísel."""

    list = []
    for i in range(number):
        randnum = random.randint(a, b)
        list.append(randnum)
    return list


# numbers = listofrandomnum(30,-5,10)
numbers = fromtxttolist("test.txt")

"""První možnost"""


def Repeat(x):
    """Nalezne a vypíše duplicity a jejich počet
        Vstup: x - list celých čísel
        Výstup: list duplicitních hodnot, počet dupl. hodnot"""

    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    duplicity = []
    for i in x:
        if i in repeated:
            duplicity.append(i)
    print(duplicity)
    pocet = len(duplicity) - len(repeated)
    print("Počet duplicit:", pocet)
    return repeated


result1 = (Repeat(numbers))


def savetotxt1(result):
    """uloží konkrétní duplicity do textového dokumentu
    Vstup: list duplicitních hodnot
    Výstup: textový soubor s názevem result"""
    print(result)
    final_result = str(result)
    final_result = final_result.replace("[", "")
    final_result = final_result.replace("]", "")
    text_file_output = open("result_1.txt", "w")
    text_file_output.write("Duplicitní číslice jsou:\n")
    text_file_output.write(final_result + "\n")
    text_file_output.close()


savetotxt1(result1)

"""Druhá možnost"""


def repeat2(numbers):
    """Nalezne a vypíše duplicity a jejich počet
        Vstup: numbers - list celých čísel
        Výstup: list duplicitních hodnot, počet dupl. hodnot"""

    sorted = list(set(numbers))
    c1 = Counter(numbers)
    c2 = Counter(sorted)
    diff = c1 - c2
    result2 = (list(diff.elements()))

    pocet = len(result2)
    print("Počet duplicit je:", pocet)
    return (result2)


result = (repeat2(numbers))


def savetotxt2(result):
    """uloží konkrétní duplicity do textového dokumentu
    navíc spočítá jejich celkový počet
    Vstup: list duplicitních hodnot
    Výstup: textový soubor s názevem result"""
    print(result)
    final_count = str(len(result))
    final_result = str(result)
    final_result = final_result.replace("[", "")
    final_result = final_result.replace("]", "")
    text_file_output = open("result.txt", "w")
    text_file_output.write("Duplicitní číslice jsou:\n")
    text_file_output.write(final_result + "\n")
    text_file_output.write("Počet duplicit:\n")
    text_file_output.write(final_count)
    text_file_output.close()


savetotxt2(result)
