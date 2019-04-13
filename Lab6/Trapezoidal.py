class Trapezoidal:
    vdeltax = 0
    deltaf =0
    def f(self, x):
        return 2 - 5*x + 10*x**2 + 0.5*x**3

    def deltax(self, a, b, n):
        self.vdeltax = (b-a)/n
        return (b-a)/n

    def CalculateTrapezoidal(self, a, b, n):
        flow = self.f(a)
        fhigh = self.f(b)
        for i in range(n-1):
            self.deltaf = self.deltaf + self.f(a+(self.vdeltax*(i+1)))
        return (self.vdeltax/2)*(flow+(2*self.deltaf)+fhigh)