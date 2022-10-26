from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Доброго времени суток: {update.effective_user.first_name}! '
                              f'\nДля получения информации о возможностях бота, введите: /help ')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\nДля сложения двух чисел введите - /sum (первое число) (второе)'
                              f'\nДля вычитания двух чисел введите - /minus (первое число, из которого нужно вычесть)  (второе)'
                              f'\nДля умножения двух чисел введите - /multiply (первое число)  (второе)'
                              f'\nДля возведения в степень числа введите - /exponentiation (первое число)  (число, в степень которого хотите возвести первое)'
                              f'\nДля деления двух чисел введите - /divide (первое число)  (второе, на которое хотите разделить первое число)'
                              f'\nПримеры: /sum 21 32 | /minus 32 10 | /exponentiation 20 2')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Время в данный момент: {datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def minus_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')


def exponentiation(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} в степени {y} = {x ** y}')


def divide_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} / {y} = {x / y}')


def multiply_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')
