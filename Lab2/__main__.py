from gcd import *
from rsa import *

rsa = Rsa()
rsa._init_(53,59)

print("n = ", rsa.calculateN())
print("phi = ", rsa.calculatephin())
e = rsa.calculateE(rsa.calculatephin())
print("e = ", e)
d = rsa.calculateD(e ,rsa.calculatephin())
print("d = ", d)
m = 123
print("m = ", m)

c = rsa.Encoding(e ,rsa.calculateN(), m)
print("Encoding c = ", c)
if(d<0):
    d = d*(-1)
print("Decoding m = ", rsa.Decoding(c, d, rsa.calculateN()))
print("--------------------")
