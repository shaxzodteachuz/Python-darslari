# 4-dars python STRING (Matn)
# Sana: 04.07.2022
# Muallif: Shaxzodjon Zoirov

ism = "Shaxzod"
print(ism)
shahar = "Jizzax"
tuman = "Sharof Rashidov"
print(tuman)
print(shahar)
matn = "Men yangi 😀 sotib oldim"
print(matn)

# String ustida amallar
ism = "Shaxzod"
print("Mening ismim " +ism)

ism = "Shaxzodjon "
familiya = "Zoirov"
# print(ism  +  familiya)
print(ism + ' ' + familiya)

#f-string

ism = "Shaxzodjon"
famliya = "Zoirov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "Shaxzodjon"
Familiya = "Zoirov"
print(f"Salom mening ismim {ism}. {ism} {familiya}!")

print("Hello world")
print("Hello \tWorld!")
print("Hello \nWorld!")

#String methodlar

ism = "Shaxzodjon"
Familiya = "Zoirov"
ism_sharif = f"{ism}  {familiya}"
print(ism_sharif.upper()) 
print(ism_sharif.title()) 
print(ism_sharif.capitalize())

meva = "  bananni    "
print(meva)
print("Men " + meva.lstrip() + "yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")

#INPUT

ism = input("Ismingiz nima?")
print("Assalomu alekum, " + ism)