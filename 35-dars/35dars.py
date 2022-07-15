# 14.07.2022
# Xatolar bilan ishlash
# Muallif: Shaxzodjon Zoirov


yosh = input("Yoshingizni kiriting:")
try:    
# try ichidagi ma'lumotlarni chiqarishga harakat qiladi.
    yosh =int(yosh)
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")
except:
# except istisno holatlarda ishlatiladi.
    print("Siz butun son kiritmadingiz")
else:
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")

print("Dastur davom etayapti")
print("Dastur tugadi")


