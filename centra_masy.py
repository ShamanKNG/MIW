import math
import random
from collections import defaultdict


def load_file(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista


def print_arr(tab):
    for i in range(len(tab)):
        print(tab[i])


def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b) ** 2
    return math.sqrt(wynik)


def random_klasa_decyzyjna(tab):
    # nadanie randomowej klasy decyzyjnej
    for i in range(len(tab)):
        tab[i][len(tab[0]) - 1] = random.randint(0, 1)


def grupowanie_po_klasach_dezyjnych(tab):
    """
    Funkcja tworzy słownik pogrupowanych wierszy po klasie decyzyjnej.
    :param tab:
    :return: {klasa_decyzyjna: [wiersze]}
    """
    slownik = defaultdict(list)
    for i in range(len(tab)):
        klasa_decyzyjna = (tab[i][len(tab[0]) - 1])
        slownik[klasa_decyzyjna].append(tab[i])
    return slownik


def suma_metryk(target, tab):
    """
    Funkcja liczy sumę odległości dla pojedyńczego wiersza
    :param target: wiersz, od którego liczone są odległości
    :param tab: tablica
    :return: suma odległości
    """
    suma = 0
    for i in range(len(tab)):
        suma += metryka_euklidesowa_wektory(target, tab[i])
    return suma


def minimalna_metryka(slownik):
    """
    Funkcja tworzy słownik z minimami sum metryk euklidesowych
    :param slownik: słownik grup
    :return: {klasa_decyzyjna: (wiersz, index_wiersza)}
    """
    slownik_minima = {}
    for key in slownik:
        wiersz = slownik[key][0]
        suma_minimum = suma_metryk(slownik[key][0], slownik[key])
        for i in range(len(slownik[key])):
            suma = suma_metryk(slownik[key][i], slownik[key])
            if suma < suma_minimum:
                suma_minimum = suma
                wiersz = slownik[key][i]
        slownik_minima[key] = wiersz
    return slownik_minima


def kolorowanie(slownik_minim, slownik_pogrupowany):
    """
    Funkcja, która zmienia klasy decyzyjne.

    Sprawdza, do której minimalnej sumy metryki euklidesa ma bliżej dany wiersz z danej grupy.
    Jeżeli wiersz ma 'bliżej' do innej klasy decyzyjnej, to zmienia klasę decyzyjną
    """
    licznik_zmian = 0
    zmiana = False
    nowy_slownik_pogrupowany = defaultdict(list)
    for klasa_decyzyjna in slownik_pogrupowany:
        for i in range(len(slownik_pogrupowany[klasa_decyzyjna])):
            wiersz = slownik_pogrupowany[klasa_decyzyjna][i]
            minimum = 0
            tmp = True
            kd = next(iter(slownik_minim))  # pierwsza klasa decyzyjna w slownk_minum
            for key in slownik_minim:
                suma = metryka_euklidesowa_wektory(wiersz, slownik_minim[key])
                if tmp:
                    minimum = suma
                    tmp = False
                elif suma < minimum:
                    minimum = suma
                    kd = key

            if wiersz[len(wiersz) - 1] != kd:  # aby nie robić powtórzeń, jeżeli klasa decyzyjna wiersza == kd
                wiersz[len(wiersz) - 1] = kd
                zmiana = True
                licznik_zmian += 1

            nowy_slownik_pogrupowany[wiersz[len(wiersz) - 1]].append(wiersz)
    return nowy_slownik_pogrupowany, zmiana, licznik_zmian


def hephaestus(plik):
    dane = load_file(plik)
    random_klasa_decyzyjna(dane)
    dane_pogrupowane = grupowanie_po_klasach_dezyjnych(dane)

    slownik_minim_tmp = minimalna_metryka(dane_pogrupowane)
    dane_pokolorowane_pogrupowane, zmiana, licznik = kolorowanie(slownik_minim_tmp, dane_pogrupowane)

    for i in range(200):
        slownik_minim = minimalna_metryka(dane_pokolorowane_pogrupowane)
        dane_pokolorowane_pogrupowane, zmiana, licznik = kolorowanie(slownik_minim, dane_pokolorowane_pogrupowane)
        print(f'Pętla: {i}')
        print(f'Minimalne wiersze: {slownik_minim}')
        print(f'Licznik zmian w kolorowaniu: {licznik}')
        print(f'Aktualne dane: {dane_pokolorowane_pogrupowane}')
        if not zmiana:
            break
    return dane_pokolorowane_pogrupowane


def zgodnosc(oryginal, hep):
    o = grupowanie_po_klasach_dezyjnych(oryginal)
    zgodnosc = 0
    for key in o:
        for wiersz in hep[key]:
            if wiersz in o[key]:
                zgodnosc += 1
    return (zgodnosc / len(oryginal)) * 100


#  ======================
slownik = hephaestus('australian.dat')
print('============== Wynik Hephaestus ==============')
for k in slownik:
    print(f'Klasa decyzyjna: {k}: {slownik[k]}')
oryginal = load_file('australian.dat')
print(f'Zgodność z oryginałem: {zgodnosc(oryginal, slownik)}%')

from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
import random
import inspect


def calculate_function_between_limits(fun, a, b, total_points, using_numpy):
    fp = {}
    if using_numpy:
        fp["x"] = np.linspace(a, b, total_points)
        fp["y"] = fun(fp["x"])
    else:
        interval = (b - a) / total_points
        fp["x"], fp["y"] = [], []
        for counter in range(total_points):
            fp["x"].append(counter * interval)
            fp["y"].append(fun(fp["x"][counter]))
    return fp


def get_max_y_from_function(y_points, using_numpy):
    fmy = 0
    if using_numpy:
        fmy = np.amax(y_points)
    else:
        fmy = max(y_points)
    return fmy


def create_random_points(total_points, a, b, max, using_numpy):
    if using_numpy:
        rp = {}
        rp["x"] = np.random.uniform(a, 3 + 0.0001, total_points)
        rp["y"] = np.random.uniform(a, max + 0.0001, total_points)
    else:
        rp = {"x": [], "y": []}
        for counter in range(total_points):
            rp["x"].append(random.uniform(a, b))
            rp["y"].append(random.uniform(0, max))
    return rp


def calculate_points_below_function(fun, random_points, using_numpy):
    points_below = 0
    if using_numpy:
        points_below = sum(random_points["y"] < fun(random_points["x"]))
    else:
        for x, y in zip(random_points["x"], random_points["y"]):
            if y < fun(x):
                points_below = points_below + 1
    return points_below


def mc_integration(fun, a, b, total_points=10000, using_numpy=False):
    function_points = calculate_function_between_limits(fun, a, b, total_points, using_numpy)
    function_max_y = get_max_y_from_function(function_points["y"], using_numpy)
    random_points = create_random_points(total_points, a, b, function_max_y, using_numpy)

    # PRINTING THE RESULTS
    print("---")
    print("::: Function: {}".format(inspect.getsource(fun).replace("    ", "")))
    print("::: Limits of Integration: {} and {}".format(a, b))
    print("::: Total Random Points:   {}".format(total_points))
    print("")
    print("::: Integration calc with Monte Carlo method:      {}".format(round(
        (calculate_points_below_function(fun, random_points, using_numpy) / total_points) * (b - a) * function_max_y,
        3)))
    print("::: Integration calc with ScyPy 'quad' function:   {}".format(round(quad(fun, a, b)[0], 3)))
    print("")
    print("::: Working with NumPy: {}".format(using_numpy))
    print("---")

    # VISUALIZATION OF THE RESULTS
    plt.plot(random_points["x"], random_points["y"], 'rx')
    plt.plot(function_points["x"], function_points["y"])
    plt.axis([a, b, 0, function_max_y])
    plt.show()


def main():
    mc_integration(lambda x: x ** 2, 0, 3, 10000, True)


# ------------------------#

main()
