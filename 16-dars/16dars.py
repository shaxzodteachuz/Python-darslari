#07.07.2022 
#Input va While
#Muallif: Shaxzodjon Zoirov

#input()



ism = input('Ismingiz nima?')
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh)
height =input("Bo'yingiz necha metr? ")
height = float(height)

son = 1
while son<=5:
    print(son, end=' ')
    son = son + 1
print("Dastur tugadi")

# while and input
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = 'Istalgan son kiriting'
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
print("Dastur tugadi!")       

# ishora
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = 'Istalgan son kiriting'
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
print("Dastur to'xtadi!")

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
    
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")
    

#Continue While
son = 0 
while son<10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)






