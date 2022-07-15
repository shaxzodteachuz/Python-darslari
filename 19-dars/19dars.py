# 07.07.2022 
# Funksiyadan qiymat qaytarish
# Muallif: Shaxzodjon Zoirov

def toliq_ism_yasa(ism, familiya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba1 = toliq_ism_yasa("olim", "olimov")
talaba2 = toliq_ism_yasa("olimov", "hakim")    
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechikib keldi")


def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
talaba1 = toliq_ism_yasa("olim", "olimov")
talaba2 = toliq_ism_yasa("hakim", "olimov", 'abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}

    avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
    avto2 = avto_info("GM", 'Gentra', 'Oq', 'Mexanika', 2016,15000)
    avtolar = [avto1, avto2]
    print('Onlayn bozordagi mavjud avtomashinalar:')
    for avto in avtolar: 
        if avto['narh']:
            narh = avto['narh']
        else:
            narh = "Noma'lum"
            print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



def oraliq(min,max, qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0,10))
print(oraliq(10,21))
