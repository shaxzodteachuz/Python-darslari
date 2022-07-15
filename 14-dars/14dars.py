# 07.07.2022
# Lug'atlar bilan ishlash  
# Muallif: Shaxzodjon Zoirov



talaba_0 = {
    'ism':'alijon',
    'familiya':'shamsiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba_0.items())

for kalit, value in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {value} \n")


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

# keys
mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
    }
print(mahsulotlar.keys())

print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
    

