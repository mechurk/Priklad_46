# Úloha číslo 46  - Dokumentace k programu 

**Zadání úkolu:** Odstranění duplicitních prvků z posloupnosti a sdělení jejich počtu.\
\
**Podrobnější zadání:** Na vstupu je nesetříděná posloupnost celých čísel. \
Nalezněte v této posloupnosti duplicitní prvky. Na výstupu je vypište  sdělte jejich počet.\
\
**Popis programu:** V programu jsou uvedeny dvě alternativní možnosti jak naleznout duplicity. \
První možnost je početně náročnější ale není potřeba importovat žádnou knihovnu. Druhá možnost obsahuje 
funkci knihovny Counter. \
\
Nejprve se pro oba programy společně vytvoří list náhodných čísel dle uživatelem zadaných parametrů.\
\
*První možnost* funguje pomocí dvou for cyklů. Jeden nalezne list jednoznačných čísel která jsou duplicitní.\
Druhý for cyklus nalezne všechna duplicitní čísla. Počet duplicitních prvků je daný rozdílem výsledků for cyklů.\
\
*Druhá (lepší) možnost* vytvoří druhý list, který je setem vstupní množiny. Následně jsou pomocí funkce counter,\
která počítá počet shodných prvků v listu, vytvořenny dva seznamy. Jeden, obsahují vstupní data a druhý obsahující\
jendoznačné hodnoty vstupních dat. Následně je vypočítán jejich rozdíl. Dále je ze seznamu vytvořen list a je \
spočítána délka tohoto listu. \
\
Pokud vstupní list neobsahuje pouze celá čísla, progam se ukončí s chybou (1).\
\
\
**Vstupní data:** List celých čísel
\
**Výstupní data:** List obsahující duplicitní prvky. Dále je vypsána informace o počtu duplicitních prvků.
\
**Testovací data:** Jsou vytvořena a testována přímo ve skriptu.
