import sys

#commandLine  python3 shift.py 5 


def decrypt(s,k):
    plain=''
    for cipher in s:
        digit=(ord(cipher)-97-k)%26
        plain+=chr(digit)
    return plain

def decrypt2(s,k):
    plain=''
    for cipher in s:
        digit=ord(cipher)*(k)%26
        plain+=chr(digit+97)
    return plain.upper()


#s='nybfxymjgjxytkynrjxnybfxymjbtwxytkynrjxnybfxymjfljtkbnxitrnybfxymjfljtkkttqnxmsjxx'
s='falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj'
#s='babab'
i=int(sys.argv[1])
inter=decrypt(s,22)
print(decrypt2(inter,15))
