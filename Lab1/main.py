from gcd import *


s = Gcd()
print("answer", s.result(1914, 899))
print("a", s.at)
print("b", s.bt)
s.egcd()
print("s", s.s)
print("t", s.t)
print("q", s.q)
w = len(s.q)-2
j = len(s.q)-1
print(((s.q[0]+s.q[w])*s.q[j])+ s.q[0])
z = []
y = []
z.append(1)
y.append(s.q[0])

for i in range(1, len(s.q)):
    c = i - 1
    z.append(y[c])
    y.append((z[i]*s.q[i])+z[c])

print(y)
print(z)
print("------------")
s = Gcd()
print("answer", s.result(93, 219))
print("a", s.at)
print("b", s.bt)
s.egcd()
print("s", s.s)
print("t", s.t)
print("q", s.q)
z = []
y = []
z.append(1)
y.append(s.q[0])

for i in range(1, len(s.q)):
    c = i - 1
    z.append(y[c])
    y.append((z[i]*s.q[i])+z[c])

print(y)
print(z)

print("------------")
numerator = input("enter numerator plz")
denumerator = input("enter denumerator plz")
s = Gcd()
print("answer", s.result(int(numerator), int(denumerator)))
print("fraction output", int(numerator) / s.result(int(numerator), int(denumerator)), "/", int(denumerator) / s.result(int(numerator), int(denumerator)))
