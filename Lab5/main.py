from MultipleNewtonRaphson import *
mnr = MNR()
x = 1.5
y = 3.5

while((abs(mnr.f1(x, y))+abs(mnr.f2(x,y)))>0.2):
    c = np.array([x, y])
    j = mnr.Jacobian(x, y)
    a = mnr.f1f2Matrix(x, y)
    z = mnr.MultiplyMatrix(mnr.CalculateInverse(j),a)
    f = mnr.SubtractMatrix(c, z)
    x = f[0]
    y = f[1]
    print(j)
    print(a)
    print(z)
    print("--------")
    print(f)
    print(x)
    print(y)
