from bot_comands import *

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


help_handler = CommandHandler('help', help)
user_login_access_handler = CommandHandler('login', user_login_access)
user_pass_access_handler = CommandHandler('pass', user_pass_access)
choose_handler = CommandHandler('choose', choose)
cl_choose_handler = CommandHandler('cl_choose', cl_choose)
all_handler = CommandHandler('all', all)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('create', u_start)],
    states={
        LOGIN: [MessageHandler(Filters.text & ~Filters.command, login)],
        END: [MessageHandler(Filters.text & ~Filters.command, end)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)


# message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(user_login_access_handler)
dispatcher.add_handler(user_pass_access_handler)
dispatcher.add_handler(choose_handler)
dispatcher.add_handler(cl_choose_handler)
dispatcher.add_handler(all_handler)

dispatcher.add_handler(conv_handler)


# dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)



print('server started')
updater.start_polling()
updater.idle()
