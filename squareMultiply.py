def sqMul(x,h,n):
    b=bin(h)[3:]    #exponent in binary
    r=x     
    for i in b:
        r=r**2 % n
        if i =='1':
            r=r*x % n
    return r

print(sqMul(1234567,2345678,3333337))
print(1234567**2345678 % 3333337)
