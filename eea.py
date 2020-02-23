import sys

__author__='Suhas Chikkanaravangala Vijayakumar'

"""
solution for multiplicative inverse using Extended euclidean Algorithm 
takes input through command line
usage: python3 eeap.y a b
   eg: python3 eea.py 1036 25
"""

def extendedEuclidean(a,b):
    A,B=a,b
    quotients=[]        #stack to store quotients
    while B!=0:
        A,B,q=B,A%B,A//B
        quotients.append(q)
    if A!=1:
        print('mutiplicative for '+str(a)+' doesnot exist')
        return
    else:
        x,y=A,B
        while quotients:
            x,y=y,x-y*quotients.pop(-1)     #pop the latest quotient
        print('multiplicative inverse of {} in mod {} is :'.format(b,a)+str(y%a))

def main():
    extendedEuclidean(int(sys.argv[1]),int(sys.argv[2]))

if __name__=='__main__':
    main()