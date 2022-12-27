from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN 
from functions import *


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

hello_handler = CommandHandler('hello', hello_function)
start_handler = CommandHandler('start', start_function)
help_handler = CommandHandler('help', help_function)
sum_handler = CommandHandler('sum', sum_function)
sub_handler = CommandHandler('sub', sub_function)
mult_handler = CommandHandler('mult', mult_function)
div_handler = CommandHandler('div', div_function)

msg_handler = MessageHandler(Filters.text, get_message)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(sub_handler)
dispatcher.add_handler(mult_handler)
dispatcher.add_handler(div_handler)

dispatcher.add_handler(msg_handler)

print('Server started')
updater.start_polling()
updater.idle()