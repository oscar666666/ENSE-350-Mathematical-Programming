from gcd import *


s = Gcd()
print("answer", s.result(1914, 899))
print("a", s.at)
print("b", s.bt)

s.egcdresult()
n = len(s.y) - 1
print("t = -", s.y[n])
print("s = ", s.z[n])
print("------------")
s = Gcd()
print("answer", s.result(22, 144))

s.egcdresult()
print("t = -", s.y[n])
print("s = ", s.z[n])

print("------------")
numerator = input("enter numerator plz")
denumerator = input("enter denumerator plz")
s = Gcd()
print("answer", s.result(int(numerator), int(denumerator)))
print("fraction output", int(int(numerator) / s.result(int(numerator), int(denumerator))), "/", int(int(denumerator) / s.result(int(numerator), int(denumerator))))
