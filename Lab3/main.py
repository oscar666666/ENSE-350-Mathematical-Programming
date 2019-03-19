from NewtonRahpson import *
from Bisection import  *
nr = NewtonRahpson()
print(nr.Function(53))
print(nr.Dfunction(53))
x = 20
nr.CalculateX(53)


bs = Bisection(0, 4)
print("f(a) = ", bs.Fuction(0))
print("f(b) = ", bs.Fuction(4))
bs.Iteritive()

bs = Bisection(-0.03, -1)
print("f(a) = ", bs.Fuction(-0.03))
print("f(b) = ", bs.Fuction(-1))
bs.Iteritive()

