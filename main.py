from typing import Any

from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram.ext import CommandHandler
TOKEN = "5769119887:AAGbCBSLXJc8oNtu2ptQhecKPpDUGaWFor4"

def echo(update,conext):
    txt = update.message.text
    if txt.lower() in ["привет","здаров"]:
        txt = "И тебе привет"

    update.message.reply_text(txt)

def start (update, conext):
    update.message.reply_text("Вас приветствует учебный бот, \n Для ыфзова помощи напишите /help")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен....")


    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()