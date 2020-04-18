from math import gcd,sqrt

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

def is_carm(n):
    """ Check whether n is a Carmichael number """
    for b in range(2, n):
        # If b is relatively prime to n
        if gcd(b, n) == 1:
            # If pow(b, n-1) % n is not 1, not Carmichael
            if pow(b, n-1, n) != 1:
                return False
    return True 

n=int(input())
res=[]
cnt=0
while cnt!=5:
    if not truePrimeChecker(n):
        if is_carm(n):
            cnt+=1
            res.append(n)
    n-=1
print(n)
print(res)
print(is_carm(res[-1]))