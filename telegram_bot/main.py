# # ************** YANGI MAVZU  ::Telegramm_bot  **********
# from transliterate import to_cyrillic , to_latin

# matn  = input("matn kiritng \n  krilchaga o'tkazib beramiz ")
# print(to_cyrillic(matn))

# matn  = input("matn kiriting. ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn)) 


                                     # TOKEN  6859209296:AAFe8iesEN3ExbVL5C7L1eJo1IKLEpYIu2o

from transliterate import to_cyrillic , to_latin
import telebot
TOKEN = '6859209296:AAFe8iesEN3ExbVL5C7L1eJo1IKLEpYIu2o'
bot = telebot.TeleBot("6859209296:AAFe8iesEN3ExbVL5C7L1eJo1IKLEpYIu2o" , parse_mode=None)
@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
    javob  = "Assalomu aleykum , xush kelibsiz !"
    javob += ' \n Bironbir suz kiritng  : Biz sizga  suzni krilchaga ugirib beramiz !' 
    bot.reply_to(message , javob )


@bot.message_handler(func=lambda  m : True)
def echo_all(message) :
    msg  =message.text
    if  msg.isascii() :
        javob = to_cyrillic(msg)
        bot.reply_to(message,javob)

    else:
        javob = to_latin(msg)
        bot.reply_to(message,javob)
bot.polling()


