class Trapezoidal:
    vdeltax = 0
    deltaf =0
    def f(self, x):
        return 2 - 5*x + 10*x**2 + 0.5*x**3

    def Intergelf(self, x):
        return 2*x -(5/2)*x**2 + (10/3)*x**3 + (0.5/4)*x**4

    def deltax(self, a, b, n):
        self.vdeltax = (b-a)/n
        return (b-a)/n

    def CalculateTrapezoidal(self, a, b, n):
        flow = self.f(a)
        fhigh = self.f(b)
        for i in range(1,n):
            self.deltaf = self.deltaf + self.f(a+(self.vdeltax*(i)))
        return (self.vdeltax/2)*(flow+(2*self.deltaf)+fhigh)
    def zero(self):
        self.vdeltax = 0
        self.deltaf = 0