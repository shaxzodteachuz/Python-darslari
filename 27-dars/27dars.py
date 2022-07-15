# 11.07.2022
# Kiril-Lotin translator bot 1-qism
# Muallif: Shaxzodjon Zoirov

from transliterate import to_cyrillic, to_latin

matn = input("Matn kiriting:")
print(to_cyrillic(matn))

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))
