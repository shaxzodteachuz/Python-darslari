# 07.07.2022
# Dictionary
# Muallif: Shaxzodjon Zoirov

car_0 = {'model': 'ferrari', 'rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':"banan"}
print(en_uz)
print(en_uz['apple'])

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':11000}
print(f"Olma narhi {mevalar['olma']} so'm")

talaba_0 = {'ism':'murod olimov', 'yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
    {talaba_0['t_yil']}-yilda tug'ilgan,\
    {talaba_0['yosh']} yoshda")
# yangi kalit va qiymat qo'shish
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'

# Bo'sh lug'at
talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Qiymatni yangilash
talaba_1['kurs'] = 4
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Kalit so'z-qiymatni o'chirib tashlash
talaba_0 = {'ism':'murod olimov', 'yosh':20,'t_yil':2000}
del talaba_0['yosh']
print(talaba_0)

# Lug'atlarni bir nechta qatorda yozish
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl'
}


