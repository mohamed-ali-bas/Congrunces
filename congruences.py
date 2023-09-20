import math 



def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

i=2
n = int(input('Number 1: '))
z = int(input("Number 2: "))



if is_coprime(n, z)==True:
 x = 1
 while i!=1:
    d=n**int(x)
    i = int(d) % int(z)
    print(n,'**',x, "[",z,"]"'->', i)
    x=x+1
