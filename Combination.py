Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def combination(l):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(l[i],l[j],l[k])
combination([1,2,3])
