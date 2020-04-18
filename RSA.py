

def sqMul(x,h,n):
    b=bin(h)[3:]    #exponent in binary
    r=x     
    for i in b:
        r=r**2 % n
        if i =='1':
            r=r*x % n
    return r

n=3763
e=11


s=[2912, 2929, 3368, 153, 3222, 3335, 153, 1222]
codebook={}
data={}
for i in range(26):
    P=i+65
    C=sqMul(P,e,n)
    codebook[C]=chr(P)
    data[chr(P)]=C


for d,v in data.items():
    print(d,' : ',v)

for j in s:
    print(codebook[j])

