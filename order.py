import sys
__author__='Suhas Chikkanaravangala Vijayakumar'

"""
solution for 
1) computing order of a modulo n ---> for all possible values of a => i.e (if gcd(a,n)=1)
2) finding primitives of modulo n.


takes input through command line
usage: python3 order.py n
   eg: python3 order.py 7
"""

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def eulersTotient(n):
    phi=0
    phis=[]
    for i in range(1,n):
        if gcd(i,n)==1:
            phi+=1
            phis.append(i)
    return phi,phis

def compute(n):
    phi,phis=eulersTotient(n)
    print(phis)
    print('phi({}) ={}'.format(n,phi))
    result={}
    for i in phis:
        gs=[]
        j=1
        while True:
            p=i**j
            mod=p%n
            gs.append(mod)
            if mod ==1:
                break
            j+=1
        result[i]=gs
    return phi,result

def main():
    phi,result=compute(int(sys.argv[1]))
    print()
    primitives=[]
    print('a | Order')
    for i,j in result.items():
        print(i,': ',j,end='  ')
        order=len(j)
        if order==phi:
            primitives.append(i)
        print(order)
    print('primitives',primitives)

if __name__=='__main__':
    main()