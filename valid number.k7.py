Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def isnumber(s: str) -> bool:
    num, exp, sign, dec=False, False, False, False
    for c in s:
        if c>='0' and c<='9': num=True
        elif c=='e' or c=='E':
            if exp or not num: return False
            else: exp, num, sign, dec=True, False, False, False
        elif c=='+' or c=='-':
            if sign or num or dec: return False
            else: sign=True
        elif c=='.':
            if dec or exp: return False
            else: dec=True
        else: return False
    return num

#main
s=input("Enter a number: ")
print(isnumber(s))

