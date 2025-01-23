from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
import os

def start(update,context):
    update.message.reply_text(
        "Iltimos rasm yuboring"
    )

def photo_handler(update,context):

    photo = update.message.photo[-1]
    inline_dislike = InlineKeyboardButton(text="👎️️️️️️",callback_data=1)
    inline_like = InlineKeyboardButton(text="👍️️️️️️",callback_data=1)
    reply_markup = InlineKeyboardMarkup([[inline_dislike,inline_like]])
    update.message.reply_photo(photo.file_id,reply_markup=reply_markup)
    

token = os.getenv('TOKEN')

updater = Updater(token=token)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',callback=start))
dispatcher.add_handler(MessageHandler(filters=Filters.photo,callback=photo_handler))

updater.start_polling()


updater.idle()