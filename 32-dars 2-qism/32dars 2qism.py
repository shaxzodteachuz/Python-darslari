# 13.07.2022
# Dunder Metodlar 2-qism
# Muallif: Shaxzodjon Zoirov


# __call__ bu method yordamida obyektni chaqirib qandaydir vazifani  bajaradigan qilish mumkin 
def __call__(self,*qiymat):
    if qiymat:
        for avto in qiymat:
            self.add_avto(avto)
    else:
        return [avto for avto in self.avtolar]

def __add__(self,boshqa_salon):
    if isinstance(boshqa_salon,AvtoSalon):
        yangi_salon = AvtoSalon(f"{self.name} {boshqa_salon.name}")
        yangi_salon.avtolar = self.avtolar + boshqa_salon.avtolar
        return yangi_salon

    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")


#__add__ - bu method qo'shish uchun ishlatiladi
#__sub__ - bu method ayirish uchun ishlatiladi
#__mul__ - bu method ko'paytirish uchun ishlatiladi
#__pow__ - bu method daraja uchun ishlatiladi
#__div__ - bu mrthod bo'lish uchun ishlatiladi



