from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
import os



def start(update,context):
    keyboard = [
        ['Marvel'],
        ["DC"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Qaysi kino studioga ovoz berasiz?",reply_markup=reply_markup
    )
def marvel(update,context):
    kinodislike = InlineKeyboardButton(text='👎️️️️️️',callback_data=1)
    kinolike = InlineKeyboardButton(text='👍️️️️️️',callback_data=1)
    kinokeyboard = InlineKeyboardMarkup([kinodislike],[kinolike])

token = os.getenv('TOKEN')

updater = Updater(token=token)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',callback=start))
updater.start_polling()
updater.idle()