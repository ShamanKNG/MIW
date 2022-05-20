import copy
import math

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

A = np.array([  # [V1,V2]
    [2, 0],
    [0, 1],
    [1, 2],
])
V1 = np.array([[0],
               [2],
               [1], ])
V2 = np.array([[1],
               [1],
               [0], ])


def prostopadla(V1, V2):
    U1 = V1
    U1T = np.transpose(U1)
    # print("U1\n", U1)
    U1len = math.sqrt(U1T @ U1)
    print("U1 długosc: ", U1len)
    ########################
    E1 = (U1) / U1len
    print(E1)
    ########################
    projU1odV2 = (np.transpose(V2) @ U1) / (np.transpose(U1) @ U1) * U1
    print(projU1odV2)
    # U2= V2 - PROJ V2
    U2 = V2 - projU1odV2
    U2T = np.transpose(U2)
    print("U2", U2)
    U2len = math.sqrt(U2T @ U2)
    print("U2 długosc: ", U2len)
    R = np.hstack((U1, U2))
    ########################
    # E2 = U2/długosc U2
    E2 = (U2) / U2len
    print(E2)
    ########################
    A = np.hstack((V1, V2))
    # R = np.hstack((U1, U2))
    Q = np.hstack((E1, E2))
    # R=Qt * A
    R = np.transpose(Q) @ A
    print("A\n", A)
    print("R\n", R)
    print("Q\n", Q)
    print("R=QT*A\n", R)
    print("A=Q*R\n", Q @ R)


prostopadla(V1, V2)

#############################
def projekcja(v, u):
    return (np.transpose(v) @ u / (np.transpose(u) @ u)) * u


def e_n(u):
    return u / math.sqrt(np.transpose(u) @ u)


def rozkład(A):
    Q = []
    u_list = []
    e_list = []
    for i in range(A.shape[1]):
        suma_projekcji = 0
        v = np.array(A[:, i]).reshape((A.shape[0], 1))
        for j in range(i):
            suma_projekcji += projekcja(v, u_list[j])
        u = v - suma_projekcji
        u_list.append(u)
        e = e_n(u)
        e_list.append(e)
        Q.append(e[:, 0])
    Q = np.array(np.transpose(Q))
    R = np.transpose(Q) @ A
    return Q, R


def a_k(A, k):
    if A.shape[0] != A.shape[1]:
        raise 'Macierze nie jest kwadratowa.'
    matrix = copy.deepcopy(A)
    for i in range(k):
        Q, R = rozkład(matrix)
        matrix = np.linalg.inv(Q) * matrix * Q
    return matrix

np.set_printoptions(suppress=True)
A = np.array([
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
])
# A = np.array([
#     [1,0],
#     [1,1],
#     [0,1],
# ])

Q, R = rozkład(A)
print(a_k(A, 2))