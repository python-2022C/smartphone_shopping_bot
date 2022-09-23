from math import inf
import telegram
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,InlineQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
import db

TOKEN = '5699418530:AAF-rw_GFSO_DeL-19T4s2eiGDXLk6OSTIg'

class Mobil_bot:
    def __init__(self) -> None:
        self.db = db.DB("db.json")

    def start(self, update:Update, context:CallbackContext):
        id = update.message.from_user.id

        keyboard_list = []
        for i in self.db.companies():
            keyboard_list.append([KeyboardButton(i)])
        keyboard = keyboard_list
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        updater.bot.sendMessage(id ,'hush kelibsiz telefon brindini tanlang', reply_markup=reply_markup)


    def bot_button(self, update:Update, context:CallbackContext):
        id = update.message.from_user.id
        text = update.message.text

        keyboard_list = []
        for i in self.db.company_mobile(text):
                keyboard_list.append([telegram.KeyboardButton(i['name'])])
        keyboard_list.append([telegram.KeyboardButton('ortga qaytish⏪')])
        keyboard = keyboard_list
        reply_markup = telegram.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        updater.bot.sendMessage(id ,'hush kelibsiz telefon brindini tanlang', reply_markup=reply_markup)


    def pone_name(self, update:Update, context:CallbackContext):
        id = update.message.from_user.id
        text = update.message.text

        if text == 'ortga qaytish⏪':
            self.start(update, context)

        elif text in self.db.pone_name():
            self.pone_imag(update,context, name = text)

        else:
            self.bot_button(update, context)

    def pone_imag(self, update:Update, context:CallbackContext, name):
        id = update.message.from_user.id
        text = update.message.text

        imeg = self.db.mobile_imeg(name)
        pone_name = self.db.mobol_info(name)['name']
        company = self.db.mobol_info(name)['company']
        price = self.db.mobol_info(name)['price']
        img_url = self.db.mobol_info(name)['img_url']
        updater.bot.sendPhoto(id, imeg, caption = f'Pone name : {pone_name}📱\n\nMobil company : {company}🧩\n\nMobil price 💵💰 : {price}\n\n\nMobel imeg url 🖼 : {img_url}')

        keyboard_list = []
        for i in self.db.company_mobile_name(company):
            keyboard_list.append([telegram.KeyboardButton(i)])
        keyboard_list.append([telegram.KeyboardButton('ortga qaytish⏪')])
        keyboard = keyboard_list
        reply_markup = telegram.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        updater.bot.sendMessage(id ,'hush kelibsiz telefon brindini tanlang', reply_markup=reply_markup)


mobil_bot = Mobil_bot()
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', mobil_bot.start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, mobil_bot.pone_name))

updater.start_polling()
updater.idle()