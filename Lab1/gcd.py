class Gcd:
    a = 0
    b = 0
    temp = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rem(self):
        self.temp = self.a % self.b
        return self.temp

    def set_ab(self, a, b):
        self.a = a
        self.b = b



