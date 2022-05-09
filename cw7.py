import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

x = np.array([
    [2],
    [5],
    [7],
    [8],
])

y = np.array([[1],
              [2],
              [3],
              [3], ])
print("y\n", y)


def fun(matrixX, matrixY):
    n = len(matrixX)
    X = np.ones((n, 1))
    X = np.hstack((X, x))
    print("X \n", X)
    B = inv(np.transpose(X) @ X) @ np.transpose(X) @ matrixY
    print("B\n", B)

    b1 = B[1][0]
    b0 = B[0][0]
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, alpha=1)
    plt.plot(x, [b0 + b1 * n for n in x])
    plt.title('Średnia Gładka')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


fun(x, y)
