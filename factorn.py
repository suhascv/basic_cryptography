import sys
from math import sqrt

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)



n=int(sys.argv[1])


for i in range(2,int(sqrt(n))+1):
    if n % i==0:
        a=n//i
        if gcd(i,a)==1:
            print(a,i)
            break
        