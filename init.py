import telebot
bot = telebot.TeleBot("5175330785:AAEOSLRDuBlTIS-4aF_BG1VpCF67FYqGVYs")

@bot.message_handler(commands=['hey'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Саня, иди нахуй!')

@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass 

print("***Бот запущен***")
bot.polling()