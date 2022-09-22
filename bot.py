from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
import os

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user_name = update.message.from_user.full_name
    keyboard = [['🇺🇿 O\'zbekcha', '🇷🇺 Русский'], ['🇺🇸 English'], ['⬅️ Orqaga']]
    update.message.reply_text(text=f"Assalomu alaykum {user_name}!\n\nTilni tanlang? | Select language?", reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))


def menu(update: Update, context: CallbackContext) -> None:
    """send services when the lang is issued."""
    if update.message.text == '🇺🇿 O\'zbekcha':
        keyboard = [['🛍 Buyurtma berish'], ['🛵 Yetkazib berish shartlari'], ['📦 Buyurtmalarim', '⚙️ Sozlamalar'], ['ℹ️ Biz haqimizda', '✍️ Fikr qoldirish']]
        update.message.reply_text('🏠 Bosh menyu', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))
    else:
        start(update, context)


dispatcher.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))
dispatcher.add_handler(handler=MessageHandler(filters=Filters.text, callback=menu))

updater.start_polling()
updater.idle()