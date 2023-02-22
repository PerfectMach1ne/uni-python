import math
import numpy as np
import pylab

if __name__ == '__main__':
    a = 3
    b = -3
    c = 4
    x = range(-10, 10) # lista argumentow x

    y = [] # lista wartosci
    for i in x:
        y.append(a * math.pow(i, 2) - b * i + c)

    pylab.plot(x, y)
    pylab.title('Wykres f(x) = a*x^2 + b*x + c')
    pylab.grid(True)
    pylab.show()
