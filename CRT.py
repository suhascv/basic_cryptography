import sys

__author__="Suhas Chikkanaravanagala Vijayakaumar"

"""
Chinise Remainder Theorem
given p,q  where 
1) p*q=n 
2) gcd(p,q)=1 or  p and q should be relatively prime.

pass p and q through command line
"""

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def phi(x):
    cnt=0
    for i in range(x):
        if gcd(i,x)==1:
            cnt+=1
    return cnt

    
def computeBasis(a,b):
    binverse=b**(phi(a)-1)%a
    return b*binverse

p=int(sys.argv[1])
q=int(sys.argv[2])
n=p*q
print('p  q','\n',p,q)

"""
computing basis 
s1=q*(q_inverse mod p) 
s2=p*(p_inverse mod q)
"""

s1=computeBasis(p,q)
s2=computeBasis(q,p)

print('basic vectors')
print(s1,s2)

"""
user inputs required n1,n2
where n1 = yournumber mod p
      n2 = yournumber mod q
"""
n1=int(input('enter n mod p : '))
n2=int(input('enter n mod q : '))

ans=(n1*s1+n2*s2) % n
print('your number is : ',ans)

