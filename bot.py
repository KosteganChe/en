from telegram.ext import Updater

def main():
    mybot = Updater("1254078369:AAEJ8jzsHrX1tkVCPUWG40RSPUjQtSBi5ZM")
    mybot.start_polling()
    mybot.idle()

main()