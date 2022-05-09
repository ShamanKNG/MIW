imie = "tomasz" #input("jak masz na imię: ")
zdanie = "cześć {}".format(imie)

print(zdanie)
print(zdanie[-1]) #jak minus to indeksuje od końca
print(zdanie[2:3]) #od którego do którego indeksu
print(zdanie[2:])   #od danego do końca
print(zdanie[:3])  #od początku do danego
print(zdanie[::3]) # krok o ile

a = "jan paweł 2"
b = 21
c = 0.37

print("typ a to {}\ntyp b to {}\ntyp c to {}".format(type(a), type(b), type(c)))
lista = ["szafa", "drzwi", "tablica", "monitor"]
lista_polaczona = "-".join(lista)
print(lista_polaczona)
lista_rozdzielona = lista_polaczona.split("-")
print(lista_rozdzielona)
print(lista_rozdzielona[2:])

q = "Metody Inżynierii Wiedzy są najlepsze"
print("Zdanie {} ma {} znaków".format(q, len(q)))
print(q.lower())
print(q.upper())

q_bez_ogonkow = q.replace("ż", "z").replace("ą", "a")
print(q_bez_ogonkow)
print("zdanie '{}' bez polskich znaków wygląda tak '{}', po zmianie ma {} znaków".format(q, q_bez_ogonkow, len(q_bez_ogonkow)))

qwe=set(q_bez_ogonkow)
print(qwe)
print(len(qwe))


q2 = "string"
q3 = 8
q4 = (q2, q3)
print(type(q4))



q5 = [1, 2, 3, 4, 5]
q6 = ["a", "b", "c", "d", "e"]
q7 = q5 + q6
print(q7)
print(q7.index(4))

print(q7)
q8 = q7.append("test")
print(q8)

print(q7)
q9 = q7.insert(8, "h")
print(q9)