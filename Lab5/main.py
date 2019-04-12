from MultipleNewtonRaphson import *
mnr = MNR()
x = 1.5
y = 3.5
c = np.array([x, y])

j = mnr.Jacobian(x, y)
a = mnr.f1f2Matrix(x, y)
z = mnr.MultiplyMatrix(mnr.CalculateInverse(j),a)
f = mnr.SubtractMatrix(c, z)
print(j)
print(a)
print(z)
print("--------")
print(f)
