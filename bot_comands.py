import json
import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN

def help(update, context):
    context.bot.send_message(update.effective_chat.id, '/help\n/login\n/password')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Incorrect command')


def user_login_access(update, context):
    global user_base
    text = context.args
    # надо пробегаться по всем именам для поиска соответствия
    count = 0
    while count < len(user_base):
        for item in user_base.values():
            for i in item.values():
                if i == text[0]:
                    context.bot.send_message(update.effective_chat.id, f'Hello, {text[0]}! Enter password (/pass)')
                    print(text[0], str(count))
                    return text[0], str(count)
            else:
                count += 1
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f'There is no {text} user in base. Try again or create new account')
        return


def user_pass_access(update, context):
    global user_base
    text = context.args
    # надо пробегаться по всем логинам для поиска соответствия
    count = 0
    while count < len(user_base):
        for item in user_base.values():
            for i in item.values():
                if i == text[0]:
                    print(text[0], str(count))
                    return text[0], str(count)
            else:
                count += 1
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f'Invalid password. Try again')
        return

path = os.path.join('Data_base', 'user_base.json')

with open(path) as file:
    global user_base
    user_base = json.load(file)
