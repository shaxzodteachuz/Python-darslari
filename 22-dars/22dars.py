# 08.07.2022
# Modullar
# Muallif: Shaxzodjon Zoirov

from avto_info_mod import avto_info, info_print

avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020, 40000)  
info_print(avto1)



import math

x=400
print(math.sqrt(x))
print(math.pow(6,2))
print(math.pi)
print(math.log2(8))
print(math.log10(100))

import random as r

son = r.randint(0,100)
print(son)


ismlar = ['olim', 'anvar', 'hasan', 'husan']
ism = r.choice(ismlar)
print(ism)
print(r.choice(ism))
x = list(range(0,51,5))
print(x)


x = list(range(11))
print(x)
r.shuffle(x)
print(x)
