import  matplotlib.pyplot as plt
import numpy as np
from Trapezoidal import *
tp = Trapezoidal()
x = np.arange(-10, 10, 0.01)
plt.plot(x, tp.f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Trapezoidal')
plt.savefig("f(x).png")
print(tp.deltax(-10, 10, 6))
print(tp.CalculateTrapezoidal(-10, 10, 6))
plt.show()