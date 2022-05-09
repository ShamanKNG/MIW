# # punkt w 14-wymiarowej przestrzeni
# # w głowie mamy ograniczenie do 3 wymiarów, żyjemy w 4,
# # przewstrzeń metryczna, potrzebna para zbiór i element
# # d - odległość
# # 1. d(a,b)= 0 => a=b
# # 2. d(a,b) = d(b,a)
# # 3. if d(a,b) + d(b,c) >= d(a,c) nierówność trókąta
# # jeżeli coś spełnia te warunki to jest to metryka, a zbiór przestrzenią metryczną
# # żeby obliczyć odległość dwóch pkt od siebie korzystamy z twierdzenia pitagorasa
# # c = pierw(a^2 + b^2)
# # (Ax - Bx)^2 + (Ay-By)^2 i im więcej wymiarów tym więcej nawiasów
# # ^rzutowanie na oś x ^rzutowanie na OY
import numpy as np
import math
#
#
#
# # lB = []
# # with open('australian.dat', 'r') as file:
# #     for line in file:
# #         lB.append(line.replace('\n','').split())
# # for el in range(5):
# #     print(lB[el])
# #
# # print(lB[:5])
# # lB = []
# # with open('australian.dat', 'r') as file:
# #     for line in file:
# #         result = list(map(lambda e: float(e), line.replace('\n', '').split()))
# #         lB.append(result)
# #         result = 0
# #
# # for el in range(5):
# #     print(lB[el])
# # print(lB[:5])
#
#
lB = []
with open('australian.dat', 'r') as file:
    for line in file:
        kolekcja = line.replace('\n', '').split()
        result = list(map(lambda e: float(e), kolekcja))
        lB.append(result)
#
# # for el in range(5):
# #     print(lB[el])
#
#
# # sqrt(pow((a-b),2)
def MetrykaEuklidesowa(listaA, listaB):

    dl = len(listaA) - 1
    tmp = 0
    for id in range(dl):
        zm1 = listaA[id]
        zm2 = listaB[id]
        c = zm1 - zm2
        wynik = c ** 2
        tmp += wynik

    result = math.sqrt(tmp)

    return result
#
# # l1 = lB[1]
# # l2 = lB[2]
# # w0 = MetrykaEuklidesowa(l1, l2)
# # print(w0)
#
# l0 = lB[0]
# l1 = lB[1]
# w0 = MetrykaEuklidesowa(l0, l1)
# print(f'Odległość 0 - 1: {w0}')
#
# w00 = MetrykaEuklidesowa(l0, l0)
# print(f'Odległość 0 - 0: {w00}')
#
# # l2 = lB[2]
# # w1 = MetrykaEuklidesowa(l0, l2)
# # print(w1)
#
# # l3 = lB[3]
# # w2 = MetrykaEuklidesowa(l0, l3)
# # print(w2)
#
# # pd
# # lista składa się z inych list
# # y = lista[0]
# # pierwszy wiersz to y
# # d(y,x), gdzie x należy do listy bez elementu z indeksem 0
# # słownik, gdzie klucz to klasa decyzyjna x(ostani element to wniosek), a wartość to lista z odległościami
# # {0 : lista z odleglosciami , 1: [], }
# # napisać funkcję która będzie liczyła wyznacznik macierzy kwadratowej i macierz moze być jako macierz albo lista list
#
#
# def Odleglosci1(lista):
#     y = lista[0]
#     s = {}
#     l_o = []
#     wynik = 0
#     for l in range(len(lista))[1:]:
#         wynik = MetrykaEuklidesowa(y, lista[l])
#         # print(f'Odległość listy {l} od y wynosi: {wynik}')
#         l_o.append(wynik)
#     return l_o
#
# # ww = Odleglosci1(lB)
# # for el in ww:
# #     print(el)
#
#
def Distance(lista):

    y = lista[0]
    s = {}

    for l in range(len(lista))[1:]:
        tmpl = lista[l]
        ost = len(tmpl) - 1
        key = int(tmpl[ost])
        wynik = MetrykaEuklidesowa(y, lista[l])
        if key not in s:
            s[key] = []
            s[key].append(wynik)
        else:
            s[key].append(wynik)
            # print(f'Odległość listy {l} od y wynosi: {wynik}')
    return s
#
#
# w = Distance(lB)
#
# for e in w:
#     print(f'klucz: {e}, wartość: {w[e]}\n')

def odl(x,lista):

    nl = []

    for l in range(len(lista)):
        tmpl = lista[l] #zapamiętuje wiersz listy
        ost = len(tmpl) - 1 #ostatni indeks z wiersza z listy
        key = int(tmpl[ost]) #pod klucz zapisuje to co kryje się pod ostatnim indeksem
        wynik = MetrykaEuklidesowa(x, lista[l])
        nnl = (key, wynik)
        nl.append(nnl)
    return nl

# x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# p = odl(x, lB)
# print(p)

def jaknatabl(x,lista):
    wynik = []
    for item in lista:
        c = item[-1]
        odl = MetrykaEuklidesowa(x, item)
        wynik.append((c, odl))
    return wynik


def listawslownik(lista):
    s = {}
    for el in lista:
        key = el[0]
        wartosc = el[1]
        if key not in s:
            s[key] = []
            s[key].append(wartosc)
        else:
            s[key].append(wartosc)
    return s

x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
p = odl(x, lB)
print(p)

t = listawslownik(p)
print(t)

def sumaodl(slownik, k):
    s = {}
    suma = 0
    for key in slownik:
        klucz = key
        listaw = slownik[klucz]
        for el in listaw[:k]:
            suma += el
            s[klucz] = suma
    return s

k = sumaodl(t, 5)
print(k)

# zrobić decyzje na podstawie sum i im mniejsza suma tym ta decyzja, jak nie to null
# zebrać to i nazwać knn

# # def wyznacznik()
# rozwinięcie laplace
# najpierw wybierasz wiersz lub kolumnę, która ma najwięcej zer, jeśli nie ma takiej, to wybieramy dowolny,
# bierzemy pierwszy wyraz wiersza i mnożymy * (-1)**(suma numeru wiersza i kolumny w której stoi dana liczba) * wyznacznik macierzy powstałej po wykreśleniu wiersza który wzięliśmy i kolumny, z której wzięliśmy wyraz,
# + itd...
# a moze zrobić jeszcze osobny dla 3x3? i użyć w tej bardziej rozbudowanej funkcji?

# 3x3
# po przekątnej od lewej do prawej dodać
# po przekątnej od prawej do lewej odejmujesz (albo od prawej do lewej tylko z dołu)
# a d g
# b e h
# c f i

# a*e*i + d*h*c + g*b*f - c*e*g - f*h*a - i*b*d


#
# k = input('Wprowadź ilość kolumn: ')
# w = input('Wprowadź ilość wierszy: ')
# q = False #kwadratowa macierz
#
# if k == w:
#     q = True
# else:
#     q = False
#     print('To nie jest macierz kwadratowa.')
# print(q)


# v = [int(input('Wprowadź wiersze macierzy: '))]
# m = np.array(v)
# print(m)


# wyznacznikiem detA macierzy A (nxn) nazywamy jedyną funkcję spełniającą następujące warunki:
# 1. detA jest liniowa względem każdej kolumny macierzy A
# 2. detA jst antysymetryczna względem zamiany dowolnej pary kolumn (jeśli dowolne kolumny zmienimy miejscami to wyzn zmienia znak)
# 3.det 1 = 1



def DetDwa(m):
    result = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return result

def DetTrzy(m):
    result = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1] \
             - m[2][0] * m[1][1] * m[0][2] - m[2][1] * m[1][2] * m[0][0] - m[2][2] * m[1][0] * m[0][1]
    return result


def ObliczWyznacznik(v, c, r):

    if c == r:
        m = np.array(v).reshape(c, r)
        print(f'Twoja macierz to:\n{m}')
        if c == 2:
            w = DetDwa(m)
            print(w)
        elif c == 3:
            w = DetTrzy(m)
            print(w)
        # else:
    else:
        print('Nie można wyliczyć wyznacznika.')

# skopiowane z neta :(
# https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
def determinant_recursive(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))

    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    # Section 3: define submatrix for focus column and
    #      call this function
    for fc in indices:  # A) for each focus column, ...
        # find the submatrix ...
        As = copy_matrix(A)  # B) make a copy, and ...
        As = As[1:]  # ... C) remove the first row
        height = len(As)  # D)

        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det

    return total


# m = np.array([[5,8],[6,9]])
# d = np.linalg.det(m)
# print(d)
# lst = [64, 5, 21, 50]
# ObliczWyznacznik(lst, 2, 2)







# dom:
# jak obliczyć metrykę euklidesową dla dwóch obiektów korzystając z wektorów i operacji na wektorach
#