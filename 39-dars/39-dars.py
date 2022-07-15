# 14.07.2022
# Python tashqi kutubxonasi
# Muallif: Shaxzodjon Zoirov

from googletrans import Translator
tarjimon = Translator() # Translator bu masus klass (tarjimon esa obyekt)

matn_uz  = "Python - dunyodagi eng mashhur dasturlash tili"

# Istalgan matnni ingliz tiliga tarjima qilish  uchun translate metodini chaqiramiz
tarjima = tarjimon.translate(matn_uz)
# Original matn
print(tarjima.text)
# Tarjima
print(tarjima.text)
# Original matn tili
print(tarjima.src)


# Boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)

# Ingliz tilidan tarjima
matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)

