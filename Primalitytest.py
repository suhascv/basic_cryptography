import random
from math import sqrt

__author__='suhas Chikkanaravangala Vijayakumar'

def gcd(a, b): 
    while(b): 
       a, b = b, a % b 
    return b


def sqMul(x,h,n):
    b=bin(h)[3:]    #exponent in binary
    r=x     
    for i in b:
        r=r**2 % n
        if i =='1':
            r=r*x % n
    return r

def truePrimeChecker(p):
    for i in range(2,int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

def primalityTest(p,s):
    for i in range(s):
        a=random.randint(1,p-2)
        if sqMul(a,p-1,p)!=1:
            return False
    return a


def isChar(n):
    a=primalityTest(n,15)
    if a:
        if not truePrimeChecker(n):
            for b in range(2, n):
                if gcd(b, n) == 1:
                    if sqMul(b, n-1, n) != 1:
                        return False
            return True
    return False

def main():
    n=int(input())
    cnt=0
    res=[]
    while n>2:  
        if isChar(n): 
            res.append(n)
            cnt+=1
        if cnt==5:
            break     
        n=n-1

    print(n)
    print(res)

if __name__=='__main__':
    main()