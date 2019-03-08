
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib.widgets import Button
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox

def polypow(poly, pow:int):
    if pow == 0: return [1]
    answer = poly.copy()
    for num in range(1, pow):
        answer = np.polymul(answer, poly)
    return answer


def binomial(n:int, k:int):
    return np.math.factorial(n)/np.math.factorial(k)/np.math.factorial(n-k)

def bezyeKoef(n , k):
    tk = np.zeros(k + 1)
    tk[0] = 1
    return binomial(n, k) * np.polymul(tk , polypow([-1, 1] , n - k))



def main():
    P = np.array([[1, 1],[2, 2],[3, 3], [4, -1], [5, 1]])
    n = len(P)
    PX = P.T[0]
    PY = P.T[1]
    x = np.zeros(n)
    y = np.zeros(n)
    for num in range(0, n):
        koef = (bezyeKoef(n - 1 , num))
        x = np.polyadd(x, P[num][0] * koef)
        y = np.polyadd(y, P[num][1] * koef)

    print("answer")
    print(x)
    print(y)

    X = []
    Y = []
    print(np.polyval(y, 0))
    for t in np.linspace(0, 1, 100):
        X += [np.polyval(x, t)]
        Y += [np.polyval(y, t)]

    print(X)
    print(Y)

    global fig, ax
    fig, ax = pylab.subplots()
    #ax = fig.gca(projection='2d')
    ax.plot(X, Y, label='parametric curve')
    ax.plot(PX, PY, label= "orientir")
    ax.legend()
    pylab.show()

if __name__ == "__main__":
    main()