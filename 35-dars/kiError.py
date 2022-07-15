# keyError lug'atlarda ishlatiladigan kalit hisoblanadi va noto'g'ri kalit ishlatilsa bu xatolik bo'ladi

user = {"username":"Shaxzodjon",
        "status":"admin",
        "email":"admin@Shaxzodjon.12",
        "phone":"998915944910"}

key="tel"
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas")

print(user['username'])