# 13.07.2022
# DUNDER Metodlar
# Muallif: Shaxzodjon Zoirov

# Dunder metodlar matnda ikkita pastki chiziqlar bilan yoziladi


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1

# __str__ bu methodga murojat qilganimizda qandaydir matnli obyekt ko'rishimiz mumkin

    def __str__(self):
            return f"Avto:  {self.make} {self.model}"
    
# __repr__ - represintation- bu method ham __str__ methodi bilan bir xil hisoblanadi.
# __repr__ - methodini ishlatishni tavsiya qilamiz, chunki bu method __str__ ga qaraganda ko'proq funksiya bilan ishlaydi.
# __str__  - methodi faqat print funksiya bilan birga keladi. 
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"

# __eq__ bu methodning kengaytirilgan varianti equal deb nomlanadi. Bu method ikta ma'lumotni bir biriga solishtirish uchun ishlatiladi.

    def __eq__(self,y):
        return self.narh==y.narh
        
    def __lt__(self,y):
        return self.narh<y.narh

# __lt__ bu methodning kengaytirilgan varinti lower then deb ataladi. 


    def __le__(self,y):
        return self.narg<=y.narh


# __len__- bu method uzunlikni qaytaradi.(length)
# __getitem__- elementlarni o'ziga oladi
# __setitem__- elementlarni almashtiramiz

    

avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,2000)

print(avto1>avto2)





    
