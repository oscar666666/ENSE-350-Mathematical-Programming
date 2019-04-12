import numpy as np

class MNR:

    def f1(self, x, y):
        return x**2 + x*y - 10

    def f2(self, x, y):
        return y + 3*x*y**2 - 57

    def df1dx(self, x, y):
        return 2*x + y

    def df1dy(self, x, y):
        return x

    def df2dx(self, x, y):
        return 3*y**2

    def df2dy(self, x, y):
        return 1 + 6*x*y

    def Jacobian(self, x, y):
        return np.array([[self.df1dx(x,y), self.df1dy(x, y)], [self.df2dx(x, y), self.df2dy(x, y)]])

    def f1f2Matrix(self, x, y):
        return np.array([self.f1(x, y),self.f2(x, y)])

    def CalculateInverse(self, x):
        return np.linalg.inv(x)

    def MultiplyMatrix(self, x, y):
        return np.dot(x,y)

    def SubtractMatrix(self, x, y):
        return np.subtract(x, y)
