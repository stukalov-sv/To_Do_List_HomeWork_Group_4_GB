from methods import check_value_is_digit_and_return_it as check
from methods import invalid_input_limit as input_limit
from Dictionaris import interface_dictionary as dic

# Вступление: краткое описание программы
def description ():
    print ('\nДанный список дел позволяет пользователям добавлять, просматривать, редактировать и удалять \
            \nсписки дел, рецепты и списки покупок, а также работать с базой и файлом лога администратору \
            \n')

# Приветствуем пользователя и выбираем опцию: Зайти под своим логином или Создать учетную запись
def input_options_log_or_create ():
    option_value = input_limit (dic.dict_options_logging)
    return option_value

# Выбор действий пользователя: работа со списками дел, рецептами или списками покупок
def input_options_user ():
    option_value = input_limit (dic.dict_options_user)
    return option_value
    
# Выбираем опцию работы со списками дел
def options_create_or_find_deals ():
    option_value = input_limit (dic.dict_start_deals)
    return option_value
    
# Выбираем опцию работы с уже существующим списком дел
def options_deals ():
    option_value = input_limit (dic.dict_options_deals)
    return option_value
    
# Выбираем опцию работы с рецептами: создать или найти
def options_create_or_find_receipt ():
    option_value = input_limit (dic.dict_start_receipt)
    return option_value
   
# Выбираем опцию работы с уже существующим рецептами
def options_receipt ():
    option_value = input_limit (dic.dict_options_receipt)
    return option_value
    
# Выбираем опцию работы со списками покупок: создать или найти
def options_create_or_find_shopping_list ():
    option_value = input_limit (dic.dict_start_shopping_list)
    return option_value

# Выбираем опцию работы с уже существующим списком покупок
def options_shopping_list ():
    option_value = input_limit (dic.dict_options_shopping_list)
    return option_value
    
# Выбор действий админа: работа с базой или с файлом лога
def input_options_admin ():
    option_value = input_limit (dic.dict_options_admin)
    return option_value
    
# Выбираем опцию работы админа с базой
def options_admin_base ():
    option_value = input_limit (dic.dict_options_admin_base)
    return option_value
    
# Выбираем опцию работы админа с файлом лога
def options_admin_log_file ():
    option_value = input_limit (dic.dict_options_admin_log)
    return option_value

# Спрашиваем о завершении работы программы или о новом действии. Если выбрано Завершение, в дальнейшем следует завершить
# программу.
def finish_options ():
    option_value = input_limit (dic.dict_options_finish)
    if option_value == 1:
        say_bye ()
    return option_value
    
# затычка - коротенькая проверка на повтор =)
def repeat_options ():
    result = input("Повторить ? y - > да / n - > нет")
    if result == "n":
        return False
    else :
        return True

# Прощаемся с пользователем
def say_bye ():
    return print(f'Всего хорошего и до скорых встреч!')

# description ()
# input_options_log_or_create ()
# input_options_user ()
# options_create_or_find_deals ()
# options_deals ()
# options_create_or_find_receipt ()
# options_receipt ()
# options_create_or_find_shopping_list ()
# options_shopping_list ()
# input_options_admin ()
# options_admin_base ()
# options_admin_log_file ()
# finish_options ()