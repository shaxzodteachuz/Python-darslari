# 06.07.2022 
# Dasturlash asoslari
# Tarmoqlanish
# Muallif: Shaxzodjon Zoirov

import logging


avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

ism = input('Ismingiz nima?/n>>>')
if ism.lower() !='ali':
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
else:
    print("Salom, Ali") 

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18:
    print('Xush kelibsiz!')
else:
    print('Kirish mumkin emas!')

login = input("Yangi login tanlang:")
if len(login)<=5:
    print("Login 5 harfdan ko'proq bo'lishi shart!")
        
