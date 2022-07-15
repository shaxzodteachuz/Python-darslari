# 14.07.2022
# JSON
# Muallif: Shaxzodjon Zoirov

# Json formati - boshida Javascript uchun yaratilgan. (Javascript Object Notation)
# Keyinchalik bu format hamma dasturlash tilida ishlatiladi. Chunki keyinchalik bu format ancha mashhur bo'lib ketadi.


# import json
# import googlemaps
# from apikey import APIKEY

# gmaps = googlemaps.Client(key=APIKEY)
# data = gmaps.geocode('Sharof Rashidov, Jizzax, Uzbekistan')

# print(data)
# g = json.dumps(data[0], indent = 4, sort_keys=True)
# print(g)


# import json 

# x = 10
# x_json = json.dumps(x)
# print(x_json)

# y = 5.5
# y_json = json.dumps(y)
# print(y_json)

import json


# json formatiga o'tkazish uchun biz dumps funksiyasidan foydalanamiz.

# m = True
# m_json = json.dumps(m)
# print(m_json)

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)
# print(sonlar_json)


bemor = {
    "ism": "Shaxzodjon Zoirov",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Shaxzod", "Shaxzodjon"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Analgin", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2}
    ]
}
bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)