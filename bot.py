from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,InlineQueryHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import db
import os

TOKEN = os.environ['TOKEN']

class Mobil_bot:
    def __init__(self) -> None:
        self.db = db.DB("db.json")
        self.index_list = 0

    def start_inlinebutton(self, update:Update, context:CallbackContext):
        inlineKeyboard1  = InlineKeyboardButton('1', callback_data=f'📱Apple')
        inlineKeyboard2  = InlineKeyboardButton('2', callback_data=f'📱Huawei')
        inlineKeyboard3  = InlineKeyboardButton('3', callback_data=f'📱Nokia')
        inlineKeyboard4  = InlineKeyboardButton('4', callback_data=f'📱Oppo')
        inlineKeyboard5  = InlineKeyboardButton('5', callback_data=f'📱Redmi')
        inlineKeyboard6  = InlineKeyboardButton('6', callback_data=f'📱Samsung')
        inlineKeyboard7  = InlineKeyboardButton('7', callback_data=f'📱Vivo')
        inline_keyboard = [
            [inlineKeyboard1,inlineKeyboard2,inlineKeyboard3,inlineKeyboard4], 
            [inlineKeyboard5,inlineKeyboard6,inlineKeyboard7]
            ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        return reply_markup

    def start_inlinebutton_text(self, update:Update, context:CallbackContext):
        buttom_str = 'Quydagi kompaniyalardan birini tallang\n\n1.Apple,\n2.Huawei,\n3.Nokia,\n4.Oppo,\n5.Redmi,\n6.Samsung,\n7.Vivo'
        return buttom_str

    def start(self, update:Update, context:CallbackContext):
        id =  update.message.chat.id
        reply_markup = self.start_inlinebutton(update,context)
        buttom_str = self.start_inlinebutton_text(update,context)
        updater.bot.sendMessage(id, buttom_str, reply_markup = reply_markup)
    def quere_start1(self, update:Update, context:CallbackContext):
        quer = update.callback_query
        quer.edit_message_caption(caption=None, reply_markup=None)
        id =  quer.message.chat_id
        reply_markup = self.start_inlinebutton(update,context)
        buttom_str = self.start_inlinebutton_text(update,context)
        updater.bot.sendMessage(id, buttom_str, reply_markup = reply_markup)

    def quere_start(self, update:Update, context:CallbackContext, x = 1,company=None):
        quere = update.callback_query
        index = self.index_list

        if company == None:
            mobil = quere.data[1:]
        
            inline_list = []
            inline_str = 'Qidirgan madilingizni tanlang\n\n'
            n = 1
            all_index = self.db.company_name(mobil, self.index_list)[1]
            for i in self.db.company_name(mobil, self.index_list)[0]:
                if n <= 5:
                    inline_str += f'{n}.{i},\n'
                    inline_list.append([InlineKeyboardButton(f'{n}', callback_data=f'📲{i}')])
                n += 1
            inline_str += f'                                    ⏪{all_index-1}/{index+1}⏩'
            inline_list.append([
                InlineKeyboardButton(f'ortga⏪', callback_data=f'⏪_{mobil}_{x}_{company}'),
                InlineKeyboardButton(f'yopish❌', callback_data=f'❌'), 
                InlineKeyboardButton(f'oldinga⏩', callback_data=f'⏩_{mobil}_{x}_{company}')])
            reply_markup = InlineKeyboardMarkup(inline_list)

            quere.edit_message_text(inline_str)
            quere.edit_message_reply_markup(reply_markup = reply_markup)

    def quere_exit(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        quere.edit_message_text(self.start_inlinebutton_text(update, context))
        quere.edit_message_reply_markup(reply_markup = self.start_inlinebutton(update, context))

    def quere_imeg(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        id = quere.from_user.id
        mobil_name = quere.data[1:]
        data = self.db.company_mobil_imeg(mobil_name)
        img_url = data[0]['img_url']
        name = data[0]['name']
        company = data[0]['company']
        color = data[0]['color']
        RAM = data[0]['RAM']
        memory = data[0]['memory']
        price = data[0]['price']

        text = f'Mobil company:{company}\n\nMobil name:{name}\nMobil color:{color}\nMobil RAM:{RAM}\nMobil memory:{memory}\nMobil price:{price}'

        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f'yopish❌', callback_data=f'🚫{company}')]])
        quere.message.reply_photo(img_url,caption=text,reply_markup=reply_markup)
        quere.edit_message_reply_markup(reply_markup=None)
        quere.edit_message_text(text='So\'ragan modilingiz surati 🖼')

    def quere_back(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        data = quere.data.split("_")
        company = data[-1]
        mobil = data[1]
        x = data[2]

        self.index_list = self.index_list -1
        index = self.index_list
        
        inline_list = []
        inline_str = 'Qidirgan madilingizni tanlang\n\n'
        n = 1
        all_index = self.db.company_name(mobil, self.index_list)[1]

        if all_index-1 > index:
            index = index
        elif all_index-1 <= index:
            self.index_list = 0
            index = self.index_list

        for i in self.db.company_name(mobil, index)[0]:
            if n <= 5:
                inline_str += f'{n}.{i},\n'
                inline_list.append([InlineKeyboardButton(f'{n}', callback_data=f'📲{i}')])
            n += 1
        inline_str += f'                                    ⏪{all_index-1}/{abs(index+1)}⏩'
        inline_list.append([
            InlineKeyboardButton(f'ortga⏪', callback_data=f'⏪_{mobil}_{x}_{company}'),
            InlineKeyboardButton(f'yopish❌', callback_data=f'❌'), 
            InlineKeyboardButton(f'oldinga⏩', callback_data=f'⏩_{mobil}_{x}_{company}')])
        reply_markup = InlineKeyboardMarkup(inline_list)

        quere.edit_message_text(inline_str)
        quere.edit_message_reply_markup(reply_markup = reply_markup)

    def quere_forward(self, update:Update, context:CallbackContext):
        quere = update.callback_query
        data = quere.data.split("_")
        company = data[-1]
        mobil = data[1]
        x = data[2]

        self.index_list = self.index_list + 1
        index = self.index_list

        inline_list = []
        inline_str = 'Qidirgan madilingizni tanlang\n\n'

        n = 1
        all_index = self.db.company_name(mobil, self.index_list)[1]
        if all_index-1 > index:
            index = index
        elif all_index-1 <= index:
            self.index_list = 0
            index = self.index_list

        for i in self.db.company_name(mobil,index)[0]:
            if n <= 5:
                inline_str += f'{n}.{i},\n'
                inline_list.append([InlineKeyboardButton(f'{n}', callback_data=f'📲{i}')])
            n += 1
        inline_str += f'                                    ⏪{all_index-1}/{abs(index+1)}⏩'
        inline_list.append([
            InlineKeyboardButton(f'ortga⏪', callback_data=f'⏪_{mobil}_{x}_{company}'),
            InlineKeyboardButton(f'yopish❌', callback_data=f'❌'), 
            InlineKeyboardButton(f'oldinga⏩', callback_data=f'⏩_{mobil}_{x}_{company}')])
        reply_markup = InlineKeyboardMarkup(inline_list)

        quere.edit_message_text(inline_str)
        quere.edit_message_reply_markup(reply_markup = reply_markup)

mobil_bot = Mobil_bot()
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', mobil_bot.start))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_start, pattern='📱'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_exit, pattern='❌'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_start1, pattern='🚫'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_back, pattern='⏪'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_forward, pattern='⏩'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobil_bot.quere_imeg ,pattern='📲'))

updater.start_polling()
updater.idle()