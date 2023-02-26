from telegram.ext import Updater,CommandHandler,CallbackQueryHandler
from handler import Mobil_bot
import os

TOKEN = os.environ['TOKEN']

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