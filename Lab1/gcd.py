class Gcd:
    def rem(self, a, b):
        return a % b

    def result(self, a, b):
        print("a", a)
        print("b", b)
        if (self.rem(a, b)) == 0:
            return b

        elif (self.rem(a, b)) == 1:
            return 1

        else:
            return self.result(b, self.rem(a, b))
