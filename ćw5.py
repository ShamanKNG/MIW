import math
import numpy as np

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


def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b) ** 2
    return math.sqrt(wynik)

v1=np.array(lista1)
# np.dot(v1,)
def metrykaeuklidesowa2(wektor1,wektor2,zm=False):
    if zm:
        v1 = np.array(wektor1)
        v2 = np.array(wektor2)
    else:
        v1 = np.array(wektor1[:-1])
        v2 = np.array(wektor2[:-1])
    wynik=np.dot(v2-v1,v2-v1)
    return math.sqrt(wynik)

print(metryka_euklidesowa_wektory([1, 2, 3], [3, 4, 6]))
print(metrykaeuklidesowa2([1, 2, 3], [3, 4, 6],True))
print(metryka_euklidesowa_wektory(lista1[0],lista1[1]))
print(metrykaeuklidesowa2(lista1[0],lista1[1],True))
print(metrykaeuklidesowa2(lista1[0],lista1[1]))
# def fun():
#     for i in range len():
#         min=0
#         suma=0



# godzina 10 min 28 lutego
