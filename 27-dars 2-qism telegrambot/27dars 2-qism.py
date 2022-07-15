# 11.07.2022
# Kiril- lotin translator telegram bot
# Muallif: Shaxzodjon Zoirov


from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5445451415:AAEoeM6U9PRJUZmV2u4Ije_610plIFXgMLM'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alekum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))       


bot.polling()

# matn = input("Matn kiriting:")    
# print(to_cyrillic(matn))


# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))

