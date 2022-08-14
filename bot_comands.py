import json
import os
from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, Filters
from config import TOKEN
from data_in_out import *
import Worck_with_base as WWB
from constants import user_data_base_path
import Dictionaris as Dic

# выводит начальный выбор команд
def help(update, context):
    context.bot.send_message(update.effective_chat.id, '/help - помощь\n'
                                                       '/start - начало авторизации\n')

# отлавливает неизвестные команды
def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, f'Incorrect command. Try /help')

# проверка соответствия логина с паролем и открытие путей работы с базой
def log_pass_check() -> bool:
    global id_login, id_pass, path_full, path_active, path_deleted, path_done
    path_full = None
    path_active = None
    path_done = None
    path_deleted = None
    if id_login == id_pass:
        path_full = WWB.path_creation_for_user_base(id_login,1,WWB.take_from_base(user_data_base_path))
        path_active = WWB.path_creation_for_user_base(id_login,2,WWB.take_from_base(user_data_base_path))
        path_done = WWB.path_creation_for_user_base(id_login,3,WWB.take_from_base(user_data_base_path))
        path_deleted = WWB.path_creation_for_user_base(id_login,4,WWB.take_from_base(user_data_base_path))
        return True
    else:
        return False

# запускает работу проверки логина и пароля
def u_start(update, _):
    update.message.reply_text(
        'Enter your login. If you do not have account - enter new login. Or /cancel to abort')
    return LOGIN

# проверяет логин и отправляет на ввод пароля, либо создание нового пароля к введенному логину
def login(update, _):
    global user_base, id_login, new_login
    count = 0
    while count < len(user_base):
        for item in user_base.values():
            for i in item.values():
                if i == update.message.text:
                    update.message.reply_text(
                        f'Hello {update.message.text}! Enter password. Or /cancel to abort')
                    id_login = str(count)
                    print(update.message.text, str(count))
                    return PASSWORD
            else:
                count += 1
    else:
        new_login = update.message.text
        update.message.reply_text(
            f'{update.message.text} - your login. Enter your password or /cancel to abort')
        return CREATE

# проверяет правильность ввода пароля
def password(update, _):
    global user_base, id_pass, approve
    count = 0
    for item in user_base.values():
        for i in item.values():
            if i == update.message.text:
                id_pass = str(count)
                print(update.message.text, str(count))
                approve = log_pass_check()
                if log_pass_check():
                    update.message.reply_text(
                        f'Now you can start to use program. Enter /choose')
                else:
                    update.message.reply_text(
                        f'Invalid password. Try again /start')
                return ConversationHandler.END
        else:
            count += 1
    else:
        update.message.reply_text(
            f'Invalid password. Try again /start')
        return ConversationHandler.END

# создает новый пароль к новому логину
def create(update, _):
    global approve, new_login
    for item in user_base.values():
        for i in item.values():
            if i == update.message.text:
                update.message.reply_text(
                    f'Invalid password, enter other password. Try again /start')
                return ConversationHandler.END
    else:
        WWB.rewrite_base_with_index_append(WWB.create_a_user(new_login, update.message.text), user_data_base_path)
        WWB.chek_for_user_base(user_data_base_path)
        WWB.foloder_for_new_user_creation(WWB.take_from_base(user_data_base_path))
        approve = True
        update.message.reply_text(
            f'{update.message.text} - your password. Now you can start to use program. Enter /choose')
        return ConversationHandler.END

# отменяет проверку логина/пароля
def cancel(update, _):
    update.message.reply_text('Good luck')
    return ConversationHandler.END

# выводит котекстное меню для работы с базой
def choose(update, context):
    if approve:
        reply_keyboard = [['Choose to view base info'], ['/all', '/active', '/done', '/deleted'],
                          ['Choose to work with base'], ['/new_card', '/find_card', '/change_card', '/delete_card'],
                          ['Shut down'], ['/cl_choose']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        update.message.reply_text("Choose what's next", reply_markup=markup_key)
    else:
        update.message.reply_text('You do not have access. Please authorize. Enter /start')

# закрывает контекстное меню для работы с базой
def cl_choose(update, _):
    update.message.reply_text('See you later', reply_markup=ReplyKeyboardRemove())


def all(update, _):
    global path_full
    if approve:
        colums_output(dct.cards_dictionary.card_id_dict, WWB.take_from_base(path_full))
    else:
        update.message.reply_text('You do not have access. Please authorize. Enter /start')


def active(update, _):
    global path_active
    if approve:
        colums_output(dct.cards_dictionary.card_id_dict, WWB.take_from_base(path_active))
    else:
        update.message.reply_text('You do not have access. Please authorize. Enter /start')


def done(update, _):
    global path_done
    if approve:
        colums_output(dct.cards_dictionary.card_id_dict, WWB.take_from_base(path_done))
    else:
        update.message.reply_text('You do not have access. Please authorize. Enter /start')


def deleted(update, _):
    global path_deleted
    if approve:
        colums_output(dct.cards_dictionary.card_id_dict, WWB.take_from_base(path_deleted))
    else:
        update.message.reply_text('You do not have access. Please authorize. Enter /start')

# начало создания карточки
def new_card(update, _):
    update.message.reply_text(
        'Enter name of card. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return NAME

# имя задачи
def name(update, _):
    global card_name
    card_name = update.message.text
    print(card_name)
    reply_keyboard = [['To Do', 'To call', 'Meeting', 'Study', 'Personal', 'Other']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Choose type of card. Or /cancel to abort', reply_markup=markup_key)
    return TOC

# тип задачи
def toc(update, _):
    global card_toc
    card_toc = update.message.text
    print(card_toc)
    update.message.reply_text(
        'Enter description. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return COMMENT

# описание задачи
def comment(update, _):
    global card_comment
    card_comment = update.message.text
    print(card_comment)
    update.message.reply_text(
        'Enter deadline (dd.mm.year). Or /cancel to abort.')
    return TIMEDO

# время выполнения
def time_to_do(update, _):
    global card_name, card_toc, card_comment
    card_ttd = update.message.text
    print(update.message.text)
    WWB.rewrite_base_with_index_append(WWB.create_a_tas_kard(card_name=card_name, type_of_card=card_toc, comment=card_comment, time_to_do=card_ttd), path_full)
    WWB.rewrite_base(WWB.copy_to_other_base(WWB.take_from_base(path_full), path_active, int(max(WWB.take_from_base(path_full).keys()))), path_active)
    reply_keyboard = [['Yes', 'No']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Something else?', reply_markup=markup_key)
    return ELSE

# запрос других операций
def some_else(update, _):
    print(update.message.text)
    if update.message.text == 'Yes':
        update.message.reply_text(
            'Enter /choose', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Good bye', reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END

# старт поиска задач
def find_card(update, _):
    reply_keyboard = [['Time_to_do', 'Type_of_card', 'Name']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Choose your search in active tasks. Or /cancel to abort', reply_markup=markup_key)
    return FIND

# значение искомого
def find(update, _):
    global find_type
    find_type = update.message.text
    print(find_type)
    update.message.reply_text(
        'What will we find. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return RELEVANCE

# вывод искомого
def relevance(update, _):
    global find_type
    find_rel = update.message.text
    print(find_rel)
    match find_type:
                # Поиск по дате
        case "Time_to_do":
            # for i in WWB.take_from_base(path_active).values():
            #     print(i["Time_to_do"])
            date = find_rel
            data = WWB.look_up_by_date(date,WWB.take_from_base(path_active))
                # Поиск по типу
        case "Type_of_card":
            # for i in WWB.take_from_base(path_active).values():
            #     print(i["Type_of_card"])
            Type = find_rel
            data = WWB.look_up_by_type(Type,WWB.take_from_base(path_active))
                # Поиск по имени
        case "Name" :
            # for i in WWB.take_from_base(path_active).values():
            #     print(i["Name"])
            name = find_rel
            data = WWB.look_up_by_name(name,WWB.take_from_base(path_active))
    print(data)
    if not data:
        update.message.reply_text(
        'Data not found , try again /find_card or /choose to new request' )
        return ConversationHandler.END
    else:
        colums_output(dict_of_rows= Dic.card_id_dict , data=data)
    reply_keyboard = [['Yes', 'No']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Something else?', reply_markup=markup_key)
    return ELSE

# старт изменения карточки
def change_card(update, _):
    update.message.reply_text(
        'Enter ID of active card, to change. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return ID_CARD

# номер ID карты для изменения
def id_card(update, _):
    global card_id
    card_id = update.message.text
    print(card_id)
    reply_keyboard = [['Name', 'Type_of_card', 'Comment', 'Time_to_do']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Choose data field to change. Or /cancel to abort', reply_markup=markup_key)
    return DATA_FIELD

# поле для изменения
def data_field(update, _):
    global card_field
    card_field = update.message.text
    print(card_field)
    update.message.reply_text(
        'Enter new data. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return DATA_CHANGE

# новые данные
def data_change(update, _):
    global card_field,card_id
    card_change = update.message.text
    print(card_change)
    WWB.rewrite_base(
    WWB.change(WWB.take_from_base(path_full), card_field, card_change,card_id), path_full)
    reply_keyboard = [['Yes', 'No']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Something else?', reply_markup=markup_key)
    return ELSE

# старт удаления карточки
def delete_card(update, _):
    update.message.reply_text(
        'Enter ID of active card, to delete. Or /cancel to abort', reply_markup=ReplyKeyboardRemove())
    return APPROVMENT

# Подтверждение удаления
def approvment(update, _):
    global remove_card
    remove_card = update.message.text
    print(remove_card)
    reply_keyboard = [['Yes', 'No']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Are you sure?', reply_markup=markup_key)
    return DEL_CARD

# функция удаления
def del_card(update, _):
    global remove_card
    print(update.message.text)
    WWB.rewrite_base(WWB.copy_to_other_base(WWB.take_from_base(path_full),path_deleted,remove_card),path_deleted)
    WWB.rewrite_base(WWB.delete_element_by_id(WWB.take_from_base(path_active),remove_card),path_active)
    update.message.reply_text(
        'Well done', reply_markup=ReplyKeyboardRemove())
    reply_keyboard = [['Yes', 'No']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(
        'Something else?', reply_markup=markup_key)
    return ELSE


global id_login, id_pass, \
    path_full, path_active, path_deleted, path_done, \
    new_login, approve, \
    card_name, card_toc, card_comment, card_ttd, \
    find_type, find_rel, \
    card_id, card_field, card_change, \
    remove_card

approve = False

LOGIN, PASSWORD, CREATE = range(3)
FIND, RELEVANCE, ELSE = range(3)
APPROVMENT, DEL_CARD, ELSE = range(3)
ID_CARD, DATA_FIELD, DATA_CHANGE, ELSE = range(4)
NAME, TOC, COMMENT, TIMEDO, ELSE = range(5)




user_path = os.path.join('Data_base', 'user_base.json')

with open(user_path) as file:
    global user_base
    user_base = json.load(file)
