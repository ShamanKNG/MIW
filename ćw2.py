zm = {
    "Czechy": "Praga",
    "Słowacja": "Bratysława",
    "Ukraina": "Kijów",
    "Nimecy": "Berlin",
    "Rosja": "Moskwa",
    'Białorus': 'Mińsk',
    'Litwa': 'Wilno',
}
print(zm)
zm["Hiszpania"] = 'Madryt'
print(zm)
print(bool(''))
print(bool(' '))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([","]))
napis = "Metody inżynierii wiedzy"
print("i" in napis)
print(napis.count('i'))
for i in range(21):
    print(i)
tmp = ''
l = []
for i in (napis):
    if (i != ' '):
        tmp += i
    else:
        l.append(tmp)
        tmp = ''
l.append(tmp)
print(l)

haslo = 'Ab1234567!'


def spr(x):
    M = 0
    m = 0
    z = 0
    for i in x:
        if (i.islower()):
            M = M + 1
        elif (i.isupper()):
            m = m + 1
        elif (i == '!'):
            z = z + 1
    if (len(x) < 10):
        return False
    elif (M == 0 or m == 0):
        return False
    elif (z == 0):
        return False
    return True


print(spr(haslo))
