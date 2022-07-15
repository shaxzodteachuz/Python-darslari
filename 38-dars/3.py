
import re
from words_list import words

word1 = "Temur"
word2 = "Tomir"
word3 = "Tulpor"


andoza = "^t...r$"
# ^ bu so'z qanday harf bilan boshlanishini ko'rsatadi
# $ bu belgi qaysi harf bilan tugashini bildiradi 

print(re.match(andoza, word1))
print(re.match(andoza, word2)) 
print(re.match(andoza, word3))


matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)

print(matches)