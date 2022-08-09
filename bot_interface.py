from bot_comands import *

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


help_handler = CommandHandler('help', help)
user_login_access_handler = CommandHandler('login', user_login_access)
user_pass_access_handler = CommandHandler('pass', user_pass_access)

# message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown)


dispatcher.add_handler(help_handler)
dispatcher.add_handler(user_login_access_handler)
dispatcher.add_handler(user_pass_access_handler)
dispatcher.add_handler(unknown_handler)
# dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()
