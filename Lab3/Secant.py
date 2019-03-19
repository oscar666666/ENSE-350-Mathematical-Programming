class Secant:
    def __init__(self, x0, x1):
        self.x0 = x0
        self.x1 = x1

    def Fuction(self, x):
        return (230*(x**4)) + (18*(x**3)) + (9*(x**2)) - (221*(x)) - 9
        #return  (x**3) - (0.165*(x**2)) + (3.9938*(10**-4))
    def CalculateRoot(self):
        temp = self.x1 - ((self.Fuction(self.x1) * (self.x1 - self.x0)) / (self.Fuction(self.x1) - self.Fuction(self.x0)))
        while abs((temp - self.x0) / temp) > 0.0001:
            temp = self.x1 - ((self.Fuction(self.x1) * (self.x1 - self.x0)) / (self.Fuction(self.x1) - self.Fuction(self.x0)))
            self.x0 = self.x1
            self.x1 = temp
            print("x = ", self.x1)


