from NewtonRahpson import *
nr = NewtonRahpson()
print(nr.Function(53))
print(nr.Dfunction(53))
x = 20
while abs(nr.Function(x)/nr.Dfunction(x)) >= 0.0001:
    x = x - (nr.Function(x)/nr.Dfunction(x))
    print("x = ", x)
