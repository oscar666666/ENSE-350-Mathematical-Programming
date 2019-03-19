import math
class NewtonRahpson:
    r = 0.9
    e0 = 8.85 * (10**-12)
    q = 2 * (10**-5)
    f = 1

    def Function(self, x):
        return ((1/(4* math.pi*self.e0))*((self.q*self.q*x)/((x**2)+(self.r**2))**(3/2)))-self.f

    def Dfunction(self, x):
        return ((-1)*(1/(4* math.pi*self.e0))*((self.q*self.q*((2*x**2) - self.r**2))/((x**2)+(self.r**2))**(5/2)))-self.f

