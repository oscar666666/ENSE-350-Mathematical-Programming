class Rsa:
    q = 0
    p = 0

    def _init_(self, q, p):
        self.p = p
        self.q = q

    def calculateN(self):
        return self.p * self.q

    def calculatephin(self):
        return (self.q - 1)*(self.p - 1)

    def calculateE(self):
        return  self.calculatephin() + 1

