from telegram.ext import Updater, CommandHandler



def greet_user(bot, update):
	text = 'Start is called'
	print(text)
	update.message.reply_text(text)

def main():
    mybot = Updater("1254078369:AAEJ8jzsHrX1tkVCPUWG40RSPUjQtSBi5ZM")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    mybot.start_polling()
    mybot.idle()

main()
