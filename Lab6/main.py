import  matplotlib.pyplot as plt
import numpy as np
from Trapezoidal import *
tp = Trapezoidal()
# x = np.arange(-10, 10, 0.01)
# plt.plot(x, tp.f(x))
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Trapezoidal')
# plt.savefig("f(x).png")
n = int(input("What is n? "))
print("delta x", tp.deltax(-10, 10, n))
print("Trapezoidal value", tp.CalculateTrapezoidal(-10, 10, n))
print("True Intergel value", tp.Intergelf(10)-tp.Intergelf(-10))
print("true percentage error",(((tp.Intergelf(10) - tp.Intergelf(-10)) - tp.CalculateTrapezoidal(-10, 10, n)) / (tp.Intergelf(10) - tp.Intergelf(-10))))
x = np.arange(1,10,1)
a = []
for i in range(1,10):
    tp.zero()
    tp.deltax(-10, 10, i)
    a.append((((tp.Intergelf(10) - tp.Intergelf(-10)) - tp.CalculateTrapezoidal(-10, 10, i)) / ((tp.Intergelf(10) - tp.Intergelf(-10)))))
#plt.plot(y, ((tp.Intergelf(10)-tp.Intergelf(-10)) - tp.CalculateTrapezoidal(-10, 10, a))/(tp.Intergelf(10)-tp.Intergelf(-10)))
plt.plot(x, a)
plt.xlabel('n')
plt.ylabel('True percentage relative error in %')
plt.title('Trapezoidal')
plt.savefig("true percentage relative error.png")
plt.show()


