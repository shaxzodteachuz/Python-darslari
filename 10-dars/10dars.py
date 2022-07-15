# 06.07.2022
# if-elif-else
# Muallif: Shaxzodjon Zoirov



son = 50
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")

yosh = int(input('Yoshingiz nechida?'))
if yosh<=4:
    narh = 0
elif yosh<=12:
    narh = 4000
elif yosh<=18:
    narh = 8000
else:
    narh = 12000

print(f"Sizga kirish {narh} so'm")

kun = input("Bugun nima kun?")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')


narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False

if choy:
    print("Mijoz choy oldi.")
    narh = narh + 3000

if salat:
    print("Mijoz salat sotib oldi")
    narh = narh + 5000

if non:
    print("Mijoz non oldi.")
    narh = narh + 2000

if kompot:
    print("Mijoz kompot sotib oldi.")
    narh = narh + 5000

if assorti:
    print("Mijoz assorti sotib oldi.")
    narh = narh + 15000

print(f"Jami {narh} so'm")

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunda ovqat yuq')