from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext,CallbackQueryHandler
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
import os
from tinydb import TinyDB,Query
res={}
reaktion = {
    'dislike': 0,
    'like':0,
    'thunder':0,
    'kaka':0,
    'fire':0
}
User= Query()
db = TinyDB('users.json')
def start(update,context):
    if update.message:
        user_id = update.message.from_user.id
        first_name = update.message.from_user.first_name
        surname = update.message.from_user.username
        if not db.search(User.user_id == user_id):
            db.insert(
                {
                    'user_id':user_id,
                    'first_name':first_name,
                    'surname' : surname
                }
            )
    update.message.reply_text(
        "Iltimos rasm yuboring\n'Malumotlar olindi.'"
    )

def photo_handler(update,context):
    photo = update.message.photo[-1]
    inline_dislike = InlineKeyboardButton(text=f"👎️️️️️ {reaktion['dislike']}",callback_data='dislike')
    inline_like = InlineKeyboardButton(text=f"👍️️️️️ {reaktion['like']}",callback_data='like')
    inline_thunder = InlineKeyboardButton(text=f"⚡️ {reaktion['thunder']}",callback_data='thunder')
    inline_kaka = InlineKeyboardButton(text=f"💩 {reaktion['kaka']}",callback_data='kaka')
    inline_fire = InlineKeyboardButton(text=f"🔥 {reaktion['fire']}",callback_data='fire')
    reply_markup = InlineKeyboardMarkup([
        [inline_dislike,inline_like],
        [inline_fire,inline_kaka],
        [inline_thunder]

    ])
    update.message.reply_photo(photo.file_id, caption="Do you like this photo?", reply_markup=reply_markup)


def button_callback(update, context):
    global reaktion
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()

    perevious_choice = res.get(user_id)

    if perevious_choice:
        reaktion[perevious_choice] -= 1
    
    new_choice = query.data

    res[user_id] = new_choice

    reaktion[new_choice] += 1



    inline_dislike = InlineKeyboardButton(text=f"👎️️️️️ {reaktion['dislike']}",callback_data='dislike')
    inline_like = InlineKeyboardButton(text=f"👍️️️️️ {reaktion['like']}",callback_data='like')
    inline_thunder = InlineKeyboardButton(text=f"⚡️ {reaktion['thunder']}",callback_data='thunder')
    inline_kaka = InlineKeyboardButton(text=f"💩 {reaktion['kaka']}",callback_data='kaka')
    inline_fire = InlineKeyboardButton(text=f"🔥 {reaktion['fire']}",callback_data='fire')
    reply_markup = InlineKeyboardMarkup([
        [inline_dislike,inline_like],
        [inline_fire,inline_kaka],
        [inline_thunder]

    ])

    query.edit_message_reply_markup(reply_markup=reply_markup)

token = os.getenv('TOKEN')

updater = Updater(token=token)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',callback=start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
updater.dispatcher.add_handler(CallbackQueryHandler(button_callback))

updater.start_polling()


updater.idle()