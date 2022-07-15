# 08.07.2022
# Funksiyalar so'ngso'z
# Muallif: Shaxzodjon Zoirov

import math

uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x, y : x ** y
print(kvadrat(3, 2))

def daraja(n):
    return lambda x: x**n


from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)


def daraja2(x):
   """Berilgan sonning kvadratini qaytaruvchi funksiya"""
   return x*x

print(list(map(daraja2,sonlar)))



kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

kvadratlar = []
for son in sonlar:
    kvadratlar.append(son*son)
print(kvadratlar)



a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)