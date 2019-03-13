class Gcd:
    gcd = 0
    sf = 0
    tf = 0
    def __init__(self):
        self.at = []
        self.bt = []
        self.s = []
        self.t = []
        self.q = []
        self.z = []
        self.y = []

    def rem(self, a, b):
        return a % b

    def result(self, a, b):

        self.at.append(a)
        self.bt.append(b)
        if (self.rem(a, b)) == 0:
            return b

        elif (self.rem(a, b)) == 1:
            self.at.append(b)
            self.bt.append(1)
            return 1

        else:
            return self.result(b, self.rem(a, b))

    def egcd(self):
        m = len(self.at)
        n = m - 1
        for i in range(1, len(self.at)):

            self.s.append(self.at[n-i])
            self.t.append(self.at[m-i])
            self.q.append(int((self.at[n-i] - self.bt[m-i]) / self.bt[n-i]))

    def egcdresult(self):
        self.z.append(1)
        self.y.append(self.q[0])

        for i in range(1, len(self.q)):
            c = i - 1
            self.z.append(self.y[c])
            self.y.append((self.z[i] * self.q[i]) + self.z[c])
