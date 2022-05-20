import copy


def new_matrix(a, i):
    arr = copy.deepcopy(a)

    if len(arr) == 2:
        return arr
    else:
        arr.pop(0)
        for j in arr:
            j.pop(i)
        return arr


def determinant(a):
    if len(a) == 1:
        return a[0]

    elif len(a) == 2:
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]

    else:
        det = 0
        for i in range(len(a[0])):
            det += ((-1) ** i) * a[0][i] * determinant(new_matrix(a, i))
        return det


A = [2]
B = [
    [1, 2, 4],
    [3, 4, 7],
    [5, 6, 7],
]
C = [
    [1, 2, 3, 4],
    [4, 3, 5, 6],
    [8, 4, 2, 1],
    [3, 2, 4, 1],
]
D = [
    [1, 3, 5, 7, 9],
    [4, 6, 3, 7, 5],
    [5, 10, 8, 3, 1],
    [1, 5, 3, 7, 6],
    [8, 1, 7, 5, 8],
]
print("Wyznacznik A = ", determinant(A))
print("Wyznacznik B = ", determinant(B))
print("Wyznacznik C = ", determinant(C))
print("Wyznacznik D = ", determinant(D))