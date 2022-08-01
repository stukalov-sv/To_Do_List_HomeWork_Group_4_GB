def chek_admin_user(user_name,pass_word = ""):
    return user_name == "admin" and pass_word == "admin"

def create_a_user():
    user_name = input("Введите имая пользователя : ")
    pass_word = input("Введите пароль : ")
    return {user_name : pass_word}

