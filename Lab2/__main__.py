from gcd import *
from rsa import *

rsa = Rsa()
rsa._init_(53, 59)

print("n = ", rsa.calculateN())
print("phi = ", rsa.calculatephin())
print("e = ", rsa.calculateE())
print("d = ", rsa.calculateD(rsa.calculatephin()))
m = 89
print("m = ", m)
print("Encoding c = ", rsa.Encoding(m))
c = rsa.Encoding(m)
print("Decoding m = ", rsa.Decoding(c))
k = rsa.Decoding(c)
print("--------------------")
gcd = Gcd()
gcd.result(3, 3016)
gcd.egcd()
gcd.egcdresult()
print(gcd.z)
print(gcd.y)