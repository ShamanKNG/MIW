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


def metrykaeuklidesowa2(wektor1, wektor2, zm=False):
    if zm:
        v1 = np.array(wektor1)
        v2 = np.array(wektor2)
    else:
        v1 = np.array(wektor1[:-1])
        v2 = np.array(wektor2[:-1])
    wynik = np.dot(v2 - v1, v2 - v1)
    return math.sqrt(wynik)


# print(metryka_euklidesowa_wektory([1, 2, 3], [3, 4, 6]))
# print(metrykaeuklidesowa2([1, 2, 3], [3, 4, 6],True))
# print(metryka_euklidesowa_wektory(lista1[0],lista1[1]))
# print(metrykaeuklidesowa2(lista1[0],lista1[1],True))
# print(metrykaeuklidesowa2(lista1[0],lista1[1]))
def srednia(wektor1, wektor2, zm=False):
    if zm:
        v1 = np.array(wektor1)
        v2 = np.array(wektor2)
    else:
        v1 = np.array(wektor1[:-1])
        v2 = np.array(wektor2[:-1])
    wynik = np.mean(v1)
    return wynik


# ///////////////////////////////////////////////
def arytm(wektor1, zm=False):
    if zm:
        lenght = len(wektor1)
    else:
        lenght = len(wektor1) - 1
    wektor2 = np.ones(lenght)
    return np.dot(wektor1, wektor2) / lenght


print("arytm: ", arytm(lista1[0], True))


def wariancja(wektor1, arytm, zm=False):
    if zm:
        lenght = len(wektor1)
    else:
        lenght = len(wektor1) - 1
    wektor2 = np.ones(lenght) * arytm
    wektor2 = wektor1 - wektor2
    return np.dot(wektor2, wektor2) / lenght


zm = wariancja(lista1[0], arytm(lista1[0], True), True)
print("Wariancja: ", wariancja(lista1[0], arytm(lista1[0], True), True), "\nOdchylenie: ",
      math.sqrt(wariancja(lista1[0], arytm(lista1[0], True), True)), "\n //////////////////")


# /////////////////////////////////////////////

def srednia2(wektor1, zm=False):
    suma = 0
    sumaw = 0
    if zm:
        lenght = len(wektor1)
    else:
        lenght = len(wektor1) - 1
    for i in range(lenght):
        suma += wektor1[i]
    for i in range(lenght):
        sumaw += (wektor1[i] - suma / lenght) ** 2
    print("Średnia arytmetyczna: ", suma / lenght, "\nWariancja: ", sumaw / lenght, "\nOdchylenie standardowe to: ",
          math.sqrt(sumaw / lenght))


srednia2(lista1[0])
srednia2(lista1[0], True)

print(srednia([1, 2, 3], [3, 4, 6]))
print(srednia([1, 2, 3], [3, 4, 6], True))
print(srednia(lista1[0], lista1[1]))
print(srednia(lista1[0], lista1[1], True))

#
# #monte carlo
# def func1(x):
#     # function f(x)=x^2
#     return x
#
#
# def mc_integrate(func, a, b, n=1000):
#     # Monte Carlo integration between x1 and x2 of given function from a to b
#
#     vals = np.random.uniform(a, b, n)
#     y = [func(val) for val in vals]
#
#     y_mean = np.sum(y) / n
#     integ = (b - a) * y_mean
#
#     return integ
#
# print(f"Monte Carlo solution: {mc_integrate(func1, 0, 1, 5000): .4f}")
#
# def rectangle(low, hight, f, n):
#     edges = np.linspace(low, hight, n)
#     area = 0
#     for r in range(len(edges)):
#         area += f(low + r*(hight-low)/n)*(hight-low)/n
#     return area
#
#
# def trig(x):
#     return x
#
#
# print("Rectangle solution: ",rectangle(0,1,trig, 100000))

# def sredniagladka():
