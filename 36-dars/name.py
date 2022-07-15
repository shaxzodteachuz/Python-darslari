# 14.07.2022
# Funksiyalarni tekshirish
# Muallif: Shaxzodjon Zoirov

def get_full_name(ism,familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}"
    else:
        return f"{ism} {familiya}".title()

print(get_full_name("Shaxzodjon",'Zoirov'))

# unittest - bu funksiya yordamida turli xil testlardan foydalanishimiz mumkin.
# test case - bitta test qilish uchun ishlatiladi.

