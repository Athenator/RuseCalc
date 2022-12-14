from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('exponentiation', exponentiation))
updater.dispatcher.add_handler(CommandHandler('minus', minus_command))
updater.dispatcher.add_handler(CommandHandler('divide', divide_command))
updater.dispatcher.add_handler(CommandHandler('multiply', multiply_command))
print('server start')
updater.start_polling()
updater.idle()
