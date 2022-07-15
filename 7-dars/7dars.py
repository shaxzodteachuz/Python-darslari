# 06.07.2022
# Dasturlash asoslari
# Tartiblash
# Muallif: Shaxzodjon Zoirov

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla']
cars.sort()
print(cars)

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla']
cars.sort(reverse=True)
print(cars)

sonlar = [12, 14, -8, -13, 45, 76, 12.4, 54,]
print(sorted(sonlar))

sonlar = [12, 14, -8, -13, 45, 76, 12.4, 54,]
sonlar.reverse()
print(sonlar)

sonlar = [12, 14, -8, -13, 45, 76, 12.4, 54,]
len(sonlar)
print(sonlar)

sonlar = list(range(0,10))
print(sonlar)

toq_sonlar = list(range(1,20,2))
print(toq_sonlar)

juft_sonlar = list(range(0,20,2))
print(juft_sonlar)

sanash =list(range(0,101,10))
print(sanash)

max_qiymat = max(toq_sonlar)
print(max_qiymat)

narhlar = [12000, 22500, 54000, 12300, 43000,32123]
arzon = min(narhlar)
qimmat = max(narhlar)
jami =sum(narhlar)
print("Eng arzon narh  ", arzon, "Eng qimmati ", qimmat, "Jami", jami,)

my_cars = cars[:]
print(cars)
print(my_cars)
my_cars.remove('volvo')
print(my_cars)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
toys = list(toys)
type(toys)
toys.append('teddy')
toys = tuple(toys)
type(toys)
print(toys)





