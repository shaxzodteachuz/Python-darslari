# 13.07.2022
# Files
# Muallif: Shaxzodjon Zoirov

# pythonda qandaydir faylni ochish uchun open funksiyasidan foydalanamiz

# Bu jarayondan foydalanish tavsiya etilmaydi
# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()


from fileinput import filename


with open('pi.txt') as file:
    pi = file.read()


print(pi)

pi = pi.strip()
pi = pi.replace('\n','')
pi = float(pi)
print(pi)



filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

# rstrip- bu method qatorning oxiridagi qandaydir belgini olib tashlash uchun ishlatiladi.
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)



faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism)
    fayl.write(str(tyil))
# str funksiya ol=rqali biz ichidagi ma'lumotni matn ko'rinishiga o'tkazib olamiz.


