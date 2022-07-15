# 14.07.2022
# Python kutubxonasi
# Muallif: Shaxzodjon Zoirov


import datetime as dt
# Datetime - vaqtlar sanalar bilan ishlatish uchun kerak bo'ladi.\

hozir = dt.datetime.now()
print(hozir) 

# dt.datetime.now - bunda hozirgi vaqt sekundgacha ko'rsatib beradi.

# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish
print(hozir.minute)
# sekundni ajratib olish
print(hozir.second)


# date- faqat sanani topishda ishlatiladi.
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2022, 7, 15)
print(f"Ertangi sana: {ertaga}")
 
# time()
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
vaqtKeyin = dt.time(14,51,30)
print(vaqtKeyin)

# Sanalar orasidagi farq
bugun = dt.date.today()
ramazon = dt.date(2022, 4, 14)
farq = ramazon-bugun
# print(farq)
print(f"Ramazonga {farq.days} kun qoldi")


# Soatlar orasida farq
hozir = dt.datetime.now()
futbol = dt.datetime(2022, 6, 13, 12, 5, 13)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")




