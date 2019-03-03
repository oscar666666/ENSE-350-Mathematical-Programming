from gcd import *

s = Gcd(1147, 899)

print(s.rem())
while True:
    if s.rem() == 0:
        print(s.b)
        break

    elif s.rem() == 1:
        print(s.b)
        break
    else:
        s.set_ab(s.b, s.rem())
        print(s.a)
