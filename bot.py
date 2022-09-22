from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, ReplyKeyboardMarkup
import os

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user_name = update.message.from_user.full_name
    update.message.reply_text(text=f"Assalomu alaykum {user_name}!\n\nTilni tanlang? | Select language?", reply_markup=ReplyKeyboardMarkup(keyboard=[['🇺🇿 O\'zbekcha', '🇷🇺 Русский'], ['🇺🇸 English'], ['⬅️ Orqaga']]))


dispatcher.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))

updater.start_polling()
updater.idle()