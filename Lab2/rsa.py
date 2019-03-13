from gcd import *
class Rsa:
    q = 0
    p = 0
    phi = 0
    n = 0
    e = 0
    d = 0
    def _init_(self, q, p):
        self.p = p
        self.q = q

    def calculateN(self):
        self.n = self.p * self.q
        return self.p * self.q

    def calculatephin(self):
        self.phi = (self.q - 1)*(self.p - 1)
        return (self.q - 1)*(self.p - 1)

    def calculateE(self):
        gcd = Gcd()
        e = 2
        while gcd.result(e, self.calculatephin())!=1:
            e=e+1
        self.e = e
        return  e

    def calculateD(self, phi):
        gcd = Gcd()
        gcd.result(self.calculateE(), phi)
        gcd.egcdresult()
        gcd.getS()
        self.d = int(((2*self.phi)+1)/self.e)
        return int(((2*self.phi)+1)/self.e)

    def Encoding(self, m):
        gcd = Gcd()

        return gcd.rem(m**self.e, self.n)

    def Decoding(self, c):
        gcd1 = Gcd()
        print("n= ", self.n)
        #print(self.fastPower(self, c, self.d, self.n))
        return gcd1.rem(c**self.d, self.n)
#self.fastPower(self, c, self.d, self.n)
            #gcd1.rem(c**self.d, self.n)
