from telegram import Update
from telegram.ext import CallbackContext
# from logging import write_log
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def hello_function(update: Update, context: CallbackContext):
    message = update.message.text
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}! Готовы увидеть чудеса?') 

def get_message(update: Update, context: CallbackContext):
    message = update.message.text
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    if 'прив' in message: 
        update.message.reply_text(f'Привет, {update.effective_user.first_name}!') 
        return
    update.message.reply_text(f'Вы ввели: {message}\n Не понял команду, повторите ввод\n')

def start_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    update.message.reply_text(f'Меня зовут Мастер комплексных чисел (общий вид комплексного числа: z = a + bi)\n'
        'Вам нужно выбрать операцию и ввести через пробел 4 числа (если число вещественное, то целая часть отделяется от дробной ".")\n'
        'Доступные действия:\n/start\n/hello\n/help - помощь\n/sum - складываю\n/sub - вычитаю\n/mult - умножаю\n/div - делю')

def help_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    update.message.reply_text(f'Доступные действия:\n/start\n/hello\n/help - помощь\n/sum - складываю\n/sub - вычитаю\n/mult - умножаю\n/div - делю')

def sum_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    if ',' in message: 
        update.message.reply_text(f'Ошибка ввода. Целая часть отделяется от дробной "." (точкой). Вы ввели {message}')
    else:
        items = message.split() # по умолчанию разбивка по пробелу, на выходе /sum 13 5 789 0.12
        if len(items) < 5:
            update.message.reply_text(f'Ошибка ввода. Нужно ввести 4 числа! Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i,\nz2 = {c} + {d}i,\nz1 + z2 = {round((a+c),4)} + {round((b+d), 4)}i')

def sub_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    if ',' in message: 
        update.message.reply_text(f'Ошибка ввода. Целая часть отделяется от дробной "." (точкой). Вы ввели {message}')
    else:
        items = message.split()
        if len(items) < 5:
            update.message.reply_text(f'Ошибка ввода. Нужно ввести 4 числа! Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i,\nz2 = {c} + {d}i,\nz1 - z2 = {round((a-c), 4)} + {round((b-d), 4)}i')

def mult_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    if ',' in message: 
        update.message.reply_text(f'Ошибка ввода. Целая часть отделяется от дробной "." (точкой). Вы ввели {message}')
    else:
        items = message.split()
        if len(items) < 5:
            update.message.reply_text(f'Ошибка ввода. Нужно ввести 4 числа! Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i,\nz2 = {c} + {d}i,\nz1 * z2 = {round((a*c - b*d), 4)} + {round((b*c + a*d), 4)}i')

def div_function(update: Update, context: CallbackContext):
    logger.info("%s: %s", update.effective_user.first_name, update.message.text)
    message = update.message.text
    if ',' in message: 
        update.message.reply_text(f'Ошибка ввода. Целая часть отделяется от дробной "." (точкой). Вы ввели {message}')
    else:
        items = message.split()
        if len(items) < 5:
            update.message.reply_text(f'Ошибка ввода. Нужно ввести 4 числа! Вы ввели {message}')    
        elif not items[1].isalpha() and not items[2].isalpha() and not items[3].isalpha() and not items[4].isalpha():
            a = float(items[1])
            b = float(items[2])
            c = float(items[3])
            d = float(items[4])

    update.message.reply_text(f'z1 = {a} + {b}i,\nz2 = {c} + {d}i,\nz1 * z2 = {round(((a*c + b*d) / (c**2 + d**2)), 4)} + {round(((b*c - a*d) / (c**2 + d**2)), 4)}i')
    