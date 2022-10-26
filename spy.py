from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime as dt


def log(update: Update, context: CallbackContext):
    time = dt.now().strftime('%H:%M')
    file = open('db.csv', 'a')
    file.write(f'{time}: {update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()