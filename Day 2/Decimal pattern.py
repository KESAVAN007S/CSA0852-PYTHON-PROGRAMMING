Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=float(input("Enter the number: ")) 
 b=int(input("Enter the number of rows: ")) 
 for i in range(b): 
     for j in range(i+1): 
         print("%.1f"%a, end=" ") 
         a = a+0.1 
     print()
