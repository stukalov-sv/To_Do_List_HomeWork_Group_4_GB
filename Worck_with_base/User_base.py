from Dictionaris import user_permissions
from Dictionaris import type_of_files_dict

# def chek_admin_user(user_name,pass_word):
#     return user_name == "admin" and pass_word == "admin"

def User_chek(user_name :str,pass_word :str,data :dict):
    data_take = dict(filter(lambda x : x[1]["User_Name"] == user_name and x[1]["Pass_word"] == pass_word  , data.items()))
    id_num = list(data_take)[0]
    return id_num,data_take[id_num]["User_Name"],data_take[id_num]["Permission"],


def create_a_user(user_name= "Test",Pass_word = "Test",perm=0,other_inf ="Some one is testing") -> dict:

    card = \
        {
            "User_Name" : user_name ,
            "Pass_word" : Pass_word ,
            "Permission" : user_permissions[perm] ,
            "Other_info" : other_inf ,
        }
    
    # print(card)
    return card

def path_creation_for_user_base(id_user : int ,type_of_base:int,data : dict) -> str:
    return f"Data_base/{id_user}_{data[id_user]['User_Name']}/{id_user}_{data[id_user]['User_Name']}_{type_of_files_dict[type_of_base]}_list.json"
  


