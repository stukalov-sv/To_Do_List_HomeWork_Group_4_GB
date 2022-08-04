def chek_admin_user(user_name,pass_word):
    return user_name == "admin" and pass_word == "admin"

def create_a_user(data_base : dict,user_Id = "",user_name= "",Pass_wordd = "",perm=0,other_inf =""):

    User_ID = max(data_base["User_ID"])+1
    User_Name = user_name
    Pass_word = Pass_wordd
    Permission = perm
    Other_info = other_inf
    return {}
