from NewtonRahpson import *
from Bisection import  *
from Secant import  *

nr = NewtonRahpson()
x = 20
print(nr.Function(x))
print(nr.Dfunction(x))

nr.CalculateX(x)

print("---------Bisection------------")

bs = Bisection(0, 1)
print("f(a) = ", bs.Fuction(0))
print("f(b) = ", bs.Fuction(1))
bs.Iteritive()
print("---------------------------")

bs = Bisection(0, -1)
print("f(a) = ", bs.Fuction(-1))
print("f(b) = ", bs.Fuction(0))
bs.Iteritive()
print("---------Secant------------")
sc = Secant(0.5, 1)
sc.CalculateRoot()
print("---------------------------")

sc = Secant(1, 0)
sc.CalculateRoot()
