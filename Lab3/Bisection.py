class Bisection:
    def __init__(self, a, b):

        self.a = a
        self.b = b

    def Fuction(self, x):
        return (230*(x**4)) + (18*(x**3)) + (9*(x**2)) - (221*(x)) - 9
        #return x**3 -3
    def CalculateRoot(self):
        m = (self.a + self.b) / 2
        if self.Fuction(m)<0:
            self.a = m
        elif self.Fuction(m)>0:
            self.b = m
        print("a = ", self.a)
        print("b = ", self.b)

    def Iteritive(self):
        while (abs(abs(self.b) - abs(self.a)) / (abs(self.a)+abs(self.b))/2) > 0.0001:
            self.CalculateRoot()