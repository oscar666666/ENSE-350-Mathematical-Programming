from gcd import *
class Rsa:

    def _init_(self, q, p):
        self.p = p
        self.q = q

    def calculateN(self):
        return self.p * self.q

    def calculatephin(self):
        return (self.q - 1)*(self.p - 1)

    def calculateE(self, phi):
        gcd = Gcd()
        e = 11
        while gcd.result(phi, e)!=1:
            e=e+1
        return  e

    def calculateD(self, e, phi):
        gcd = Gcd()
        gcd.result(e, phi)
        gcd.egcd()
        gcd.egcdresult()

        return gcd.z[len(gcd.z)-1]

    def Encoding(self, e, n, m):
        gcd = Gcd()
        return gcd.rem(m**e, n)

    def Decoding(self, c, d, n):
        e =(c**d)% n
        return e

    def powmod(self):
        accum = 1;
        i = 0;
        apow2 = self.c
        self.d = (-1)*self.d
        while ((self.d >> i) > 0):
            if ((self.d >> i) & 1):
                accum = (accum * apow2) % self.n
            apow2 = (apow2 * apow2) % self.n
            i += 1
        return accum
#self.fastPower(self, c, self.d, self.n)
            #gcd1.rem(c**self.d, self.n)
