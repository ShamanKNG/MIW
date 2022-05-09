import math

lista = []
lista1 = []
with open("australian.dat") as f:
    for i in f:
        # lista.append(i.split())
        wynik = list(map(lambda e: float(e), i.split()))
        lista1.append(wynik)

for i in range(5):
    # print(lista[i])
    print(lista1[i])


def MetrykaEuklidesowa(listA, listB):
    suma = 0
    for i in range(len(listA)-1):
        suma += (pow(listA[i]-listB[i],2))
    return math.sqrt(suma)


MetrykaEuklidesowa(lista1[0], lista1[1])
MetrykaEuklidesowa(lista1[0], lista1[2])
MetrykaEuklidesowa(lista1[0], lista1[3])

# y=lista[0]
# d(y,x) gdzie x e lista bez elementu z idnexem 0
# słwonik{klasa decyzyjna(ostatni element x) :  lista z odległosciami
# }
#
#
# napisac funckje liczacy wyznacznik macierzy kwadratowej

###################################################################################
# ZADANIE                                                                         #
# obliczanie metryki euklidesowej korzystając z wektorów i operacji na wektorach  #
###################################################################################
import math
import numpy as np


def MetrykaEuklidesowa(lista0, listaX):
    dist = 0
    for i in range(0, len(lista0) - 1):
        dist += pow(lista0[i] - listaX[i], 2)
    return math.sqrt(dist)


def MetrykaNaWektorach(lista0, listaX):
    return math.sqrt(sum((e1-e2)**2 for e1, e2 in zip(lista0, listaX)))


lista = []

with open('australian.dat', 'r') as auData:
    for line in auData:
        kolekcja = line.replace('\n', '').split()
        wynik = list(map(lambda e: float(e), kolekcja))
        lista.append(wynik)

# tworzę pustą listę potrzebną do stworzenia listy unikalnych kluczy
keyes = []

# do listy z kluczami dodaję po kolei każdą wartość decyzyjną wiersza
for i in range(0, len(lista)):
    keyes.append(lista[i][len(lista[i]) - 1])

# tworzę zbiór na podstawie listy kluczy, tym samym eliminując duplikaty
keySet = set(keyes)

# Tworzę słownik zawierający klucze z wcześniej utworzonego zbioru
# do każdego klucza przypisuję pustą listę, która będzie zawierała odległości wszystkich wierszy od wiersza pierwszego
dict = {}
for i in keySet:
    dict[i] = []

list0 = lista[0]

# Przechodzę po każdym elemencie listy, oprócz pierwszego, za pomocą .append()
# dodaję do listy przypisanej do klucza o wartości takiej jak wartość decyzyjna wiersza
# odległość między aktualnym wierszem a wierszem pierwszym
for i in range(1, 7):
    listB = lista[i]
    dict[listB[(len(listB) - 1)]].append(MetrykaNaWektorach(list0, listB))

print(dict)