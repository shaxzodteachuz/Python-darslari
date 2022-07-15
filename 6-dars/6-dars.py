# 05.07.2022 
# Dasturlash asoslari
# List
# Muallif: Shaxzodjon Zoirov

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("qulupnay")
print(mevalar) 
narhlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
narhlar.insert(0, "20000")
print(narhlar)
sonlar = ['bir', 'ikki', 3, 4, 5]
sonlar.remove("ikki")
print(sonlar)
del sonlar [0]  
print(sonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
mahsulot = bozorlik.pop()
print("Men " + mahsulot +  " sotib oldim") 
print("Olinmagan mahsulotlar:", bozorlik)