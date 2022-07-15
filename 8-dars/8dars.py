# 06.07.2022
# Dasturlash asoslari
# Muallif: Shaxzodjon Zoirov
# For Loop

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim',]
for mehmon in mehmonlar:
    print("Salom", mehmon)
    print("Hayr,", mehmon)

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 19-iyul kuni Shohjahonning tug'ilgan kuniga tashrif buyurishingizni istab qolamiz")
    print("Hurmat bilan, It Park")

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")


dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:"))
    print(dostlar)
    