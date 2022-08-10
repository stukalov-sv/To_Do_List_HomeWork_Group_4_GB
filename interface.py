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
    
def input_options_what_to_do (opt_inquiry = '\nЧто хотите сделать? Найти дело [1],  Создать дело [2] Вывести список дел [3]: ',
                        opt_1 = 'Ищем дело .\n',
                        opt_2 = 'Создаём дело.\n',
                        opt_3 = 'Будем выводит список дел.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        elif option_value == 3:
            print (opt_3)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value 
def input_options_how_to_find (opt_inquiry = '\nКак будем искать дело? По дате [1],  По Типу [2] По названию [3]: ',
                        opt_1 = 'Ищем дело по дате .\n',
                        opt_2 = 'Ищем дело по типу.\n',
                        opt_3 = 'Ищем дело по названию.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        elif option_value == 3:
            print (opt_3)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value   

# Выбираем опцию работы со списками дел
def options_create_or_find_deals ( opt_inquiry = 'Будете создавать новую задачу или искать уже созданную? Создать [1],  Поиск задачи для просмотра/изменения/удаления [2]: ',
                                opt_1 = 'Создать новый список дел.\n',
                                opt_2 = 'Просмотреть весь список дел.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
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
    

# def repeat_options (user_name,
#                         opt_inquiry = 'Повторить последнюю задачу? Да [1] или Нет [2]: ',
#                         opt_1 = 'Повторяем.\n',
#                         opt_2 = 'Прошли.\n'):
#     count = 0
#     while count < 3:
#         option_value = check(opt_inquiry)
#         if option_value == 1:
#             print (opt_1)
#             say_bye (user_name)
#             break
#         elif option_value == 2:
#             print (opt_2)
#             break
#         else:
#             print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
#             count +=1
#     return option_value

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