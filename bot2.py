import telebot

bot = telebot.TeleBot('1254078369:AAEJ8jzsHrX1tkVCPUWG40RSPUjQtSBi5ZM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()