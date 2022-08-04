from methods import check_value_is_digit_and_return_it as check

# Вступление: краткое описание программы
def description ():
    print ('\nДанный список дел позволяет пользователям добавлять, просматривать, редактировать и удалять \
            \nсписки дел, рецепты и списки покупок, а также работать с базой и файлом лога администратору \
            \n')

# Приветствуем пользователя и выбираем опцию: Зайти под своим логином или Создать учетную запись
def input_options_log_or_create (opt_inquiry = '\nДоброго времени суток! Можете зайти в программу под своим логином [1] или Создать новую учетную запись [2]: ',
                                opt_1 = 'Зайти под своим логином.\n',
                                opt_2 = 'Созание новой учетной записи.\n'):
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

# Выбор действий пользователя: работа со списками дел, рецептами или списками покупок
def input_options_user (opt_inquiry = '\nС чем хотите поработать? Списки дел [1],  Рецепты [2] или Списки покупок [3]: ',
                        opt_1 = 'Работа со списками дел.\n',
                        opt_2 = 'Работа с рецептами.\n',
                        opt_3 = 'Работа со списками покупок.\n'):
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
                                opt_2 = 'Найти уже созданный список дел.\n'):
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
def options_deals ( opt_inquiry = 'Искомый список найден? Что требуется сделать? Посмотреть [1], Редактировать [2] или Удалить [3]: ',
                    opt_1 = 'Просмотр списка дел.\n',
                    opt_2 = 'Редактирование списка дел.\n',
                    opt_3 = 'Удаление списка дел.\n'):
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

# Выбираем опцию работы с рецептами: создать или найти
def options_create_or_find_receipt (opt_inquiry = 'Нашли новый рецепт или будете готовить? Создать новый рецепт [1] или Поиск рецепта для просмотра/изменения/удаления [2]: ',
                                    opt_1 = 'Создать новый рецепт.\n',
                                    opt_2 = 'Найти уже созданный рецепт.\n'):
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

# Выбираем опцию работы с уже существующим рецептами
def options_receipt (opt_inquiry = 'Искомый рецепт найден. Что требуется сделать? Посмотреть [1], Редактировать [2] или Удалить [3]: ',
                    opt_1 = 'Просмотр рецепта.\n',
                    opt_2 = 'Редактирование рецепта.\n',
                    opt_3 = 'Удаление рецепта.\n'):
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

# Выбираем опцию работы со списками покупок: создать или найти
def options_create_or_find_shopping_list (opt_inquiry = 'Будете создавать новый список покупок или искать уже созданный? Создать [1],  Поиск списка покупок для просмотра/изменения/удаления [2]: ',
                                            opt_1 = 'Создать новый список покупок.\n',
                                            opt_2 = 'Найти уже созданный список покупок.\n'):
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

# Выбираем опцию работы с уже существующим списком покупок
def options_shopping_list ( opt_inquiry = 'Искомый список найден. Что требуется сделать? Посмотреть [1], Редактировать [2] или Удалить [3]: ',
                            opt_1 = 'Просмотр списка покупок.\n',
                            opt_2 = 'Редактирование списка покупок.\n',
                            opt_3 = 'Удаление списка покупок.\n'):
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


# Выбор действий админа: работа с базой или с файлом лога
def input_options_admin (opt_inquiry = '\nПривет, админ! С чем хочешь поработать? База записей [1] или Файл лога [2]: ',
                        opt_1 = 'Работа с базой записей.\n',
                        opt_2 = 'Работа с файлом лога.\n'):
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

# Выбираем опцию работы админа с базой
def options_admin_base (opt_inquiry = 'Что будешь делать дальше? Сортировка для дальнейшей обработки [1], Просмотр [2] или Блокировка контакта [3]: ',
                        opt_1 = 'Сортировка БД.\n',
                        opt_2 = 'Просмотр БД.\n',
                        opt_3 = 'Блокировка контакта.\n'):
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

# Выбираем опцию работы админа с файлом лога
def options_admin_log_file (opt_inquiry = 'Что требуется сделать с файлом? Просто посмотреть [1] или Изменить [2]: ',
                            opt_1 = 'Просмотр лога.\n',
                            opt_2 = 'Изменение файла лога.\n'):
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


# Спрашиваем о завершении работы программы или о новом действии. Если выбрано Завершение, в дальнейшем следует завершить
# программу.
def finish_options (opt_inquiry = 'Вы закончили работу со списком задач? Да, завершить работу [1] или Нет, я хочу поработать еще [2]: ',
                        opt_1 = 'Завершение работы. Выход из программы.\n',
                        opt_2 = 'Продолжаем работу.\n'):
    count = 0
    while count < 3:
        option_value = check(opt_inquiry)
        if option_value == 1:
            print (opt_1)
            say_bye (user_name)
            break
        elif option_value == 2:
            print (opt_2)
            break
        else:
            print(f'Неверный ввод. У вас осталось {2-count} попыток ввода')
            count +=1
    return option_value

# затычка - коротенькая проверка на повтор =)
def repeat_options ():
    result = input("Повторить ? y - > да / n - > нет")
    if result == "n":
        return False
    else :
        return True

# Прощаемся с пользователем
def say_bye (user_name):
    return print(f'Всего хорошего и до скорых встреч, {user_name}!')


