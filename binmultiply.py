import sys

"""
perform mixed column and inverse mixed column operation of AES.
input format 
1st row of constant matrix as first 4 arguments
any single column state matrix next 4 arguments
eg:     
python3 binmultiply.py 02 03 01 01 87 6E 46 A6
"""

__author__='Suhas_CV'

def multiply(a,b):
    
    sum=0
    while a and b:
        if b&1:
            sum=sum^a
        
        if(a & 0x80):
            a=(a<<1)^0x11b
        else:
            a<<=1
        b>>=1
    return sum
    
def add(ps):
    s=0
    for p in ps:
        s=s^p
        if s >=283:
            s=s^0x11b
    
    return hex(s)

a1=int('0x'+sys.argv[1],16)
a2=int('0x'+sys.argv[2],16)
a3=int('0x'+sys.argv[3],16)
a4=int('0x'+sys.argv[4],16)

b1=int('0x'+sys.argv[5],16)
b2=int('0x'+sys.argv[6],16)
b3=int('0x'+sys.argv[7],16)
b4=int('0x'+sys.argv[8],16)


for i in range(4):
    p1=multiply(a1,b1)
    p2=multiply(a2,b2)
    p3=multiply(a3,b3)
    p4=multiply(a4,b4)
    a1,a2,a3,a4=a4,a1,a2,a3


    print(add([p1,p2,p3,p4]))
