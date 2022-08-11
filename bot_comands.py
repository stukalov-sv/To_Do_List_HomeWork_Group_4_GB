import json
import os
from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, Filters
from config import TOKEN
from data_in_out import *


def help(update, context):
    context.bot.send_message(update.effective_chat.id, '/help - помощь\n'
                                                       '/login логин - ввод логина\n'
                                                       '/pass пароль - ввод пароля\n'
                                                       '/create - создание аккаунта\n')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Incorrect command')


def user_login_access(update, context):
    global user_base, id_login
    text = context.args
    count = 0
    while count < len(user_base):
        for item in user_base.values():
            for i in item.values():
                if i == text[0]:
                    context.bot.send_message(update.effective_chat.id,
                                             f'Hello, {text[0]}! Enter password (/pass password)')
                    id_login = str(count)
                    print(text[0], str(count))
                    return text[0], str(count)
            else:
                count += 1
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f'There is no {text} user in base. Try again or /create new account')
        return


def user_pass_access(update, context):
    global user_base, id_pass
    text = context.args
    count = 0
    while count < len(user_base):
        for item in user_base.values():
            for i in item.values():
                if i == text[0]:
                    id_pass = str(count)
                    print(text[0], str(count))
                    return text[0], str(count)
            else:
                count += 1
    else:
        context.bot.send_message(update.effective_chat.id,
                                 f'Invalid password. Try again')
        return


def log_pass_check() -> bool:
    global id_login, id_pass
    if id_login == id_pass:
        return True
    else:
        return False


def u_start(update, _):
    update.message.reply_text(
        'Enter your login or /cancel to cancel')
    return LOGIN


def login(update, _):
    global user_base
    print(update.message.text)
    for item in user_base.values():
        for i in item.values():
            if i == update.message.text:
                update.message.reply_text(
                    f'There is {update.message.text} user already in base. Try again /create')
                return ConversationHandler.END
            else:
                update.message.reply_text(
                    f'{update.message.text} - your login. Enter your password or /cancel to cancel')
                return END


def end(update, _):
    print(update.message.text)
    update.message.reply_text(
        f'{update.message.text} - your password. Now you can start to use program')
    return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text('Good luck')
    return ConversationHandler.END


def choose(update, context):
    reply_keyboard = [['/all', '/active'], ['/done', '/deleted'], ['/cl_choose']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Choose what's next", reply_markup=markup_key)


def cl_choose(update, _):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


# def add(update, context):

def all(update, _):
    colums_output(dct.cards_dictionary.card_id_dict, test_card_bot)


global id_login, id_pass

LOGIN, END = range(2)

user_path = os.path.join('Data_base', 'user_base.json')

with open(user_path) as file:
    global user_base
    user_base = json.load(file)


test_path = os.path.join('Data_base', '1_Test', '1_Test_full_list.json')

with open(test_path) as file:
    global test_card_bot
    test_card_bot = json.load(file)