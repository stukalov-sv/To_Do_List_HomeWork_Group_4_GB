from bot_comands import *

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

help_handler = CommandHandler('help', help)
choose_handler = CommandHandler('choose', choose)
all_handler = CommandHandler('all', all)
active_handler = CommandHandler('active', active)
done_handler = CommandHandler('done', done)
deleted_handler = CommandHandler('deleted', deleted)
cl_choose_handler = CommandHandler('cl_choose', cl_choose)

conv_handler_login = ConversationHandler(
    entry_points=[CommandHandler('start', u_start)],
    states={
        LOGIN: [MessageHandler(Filters.text & ~Filters.command, login)],
        PASSWORD: [MessageHandler(Filters.text & ~Filters.command, password)],
        CREATE: [MessageHandler(Filters.text & ~Filters.command, create)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

conv_handler_new_card = ConversationHandler(
    entry_points=[CommandHandler('new_card', new_card)],
    states={
        NAME: [MessageHandler(Filters.text & ~Filters.command, name)],
        TOC: [MessageHandler(Filters.regex('^(To Do|To call|Meeting|Study|Personal|Other)$'), toc)],
        COMMENT: [MessageHandler(Filters.text & ~Filters.command, comment)],
        TIMEDO: [MessageHandler(Filters.text & ~Filters.command, time_to_do)],
        ELSE: [MessageHandler(Filters.regex('^(Yes|No)$'), some_else)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

conv_handler_find_card = ConversationHandler(
    entry_points=[CommandHandler('find_card', find_card)],
    states={
        FIND: [MessageHandler(Filters.regex('^(Time_to_do|Type_of_card|Name)$'), find)],
        RELEVANCE: [MessageHandler(Filters.text & ~Filters.command, relevance)],
        ELSE: [MessageHandler(Filters.regex('^(Yes|No)$'), some_else)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

conv_handler_change_card = ConversationHandler(
    entry_points=[CommandHandler('change_card', change_card)],
    states={
        ID_CARD: [MessageHandler(Filters.text & ~Filters.command, id_card)],
        DATA_FIELD: [MessageHandler(Filters.regex('^(Name|Type_of_card|Comment|Time_to_do)$'), data_field)],
        DATA_CHANGE: [MessageHandler(Filters.text & ~Filters.command, data_change)],
        ELSE: [MessageHandler(Filters.regex('^(Yes|No)$'), some_else)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

conv_handler_delete_card = ConversationHandler(
    entry_points=[CommandHandler('delete_card', delete_card)],
    states={
        APPROVMENT: [MessageHandler(Filters.text & ~Filters.command, approvment)],
        DEL_CARD: [MessageHandler(Filters.regex('^(Yes|No)$'), del_card)],
        ELSE: [MessageHandler(Filters.regex('^(Yes|No)$'), some_else)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

# message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(help_handler)
dispatcher.add_handler(choose_handler)
dispatcher.add_handler(all_handler)
dispatcher.add_handler(active_handler)
dispatcher.add_handler(done_handler)
dispatcher.add_handler(deleted_handler)
dispatcher.add_handler(cl_choose_handler)

dispatcher.add_handler(conv_handler_login)
dispatcher.add_handler(conv_handler_new_card)
dispatcher.add_handler(conv_handler_find_card)
dispatcher.add_handler(conv_handler_change_card)
dispatcher.add_handler(conv_handler_delete_card)

# dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)


print('server started')
updater.start_polling()
updater.idle()
