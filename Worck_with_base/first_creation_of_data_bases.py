import json
import os

from Dictionaris import user_permissions
from Dictionaris import type_of_files_dict



def create_new_base(dictionary : dict , path : str):
        with open(path, 'w') as outfile:
            json.dump(dictionary, outfile,indent=2)
            outfile.close()

def create_a_base(path):
    file = open(path , 'w')
    file.close()

def chek_for_user_base(path):
    if not os.path.exists(path):
        create_a_base(path)
        card = \
            {
                "User_Name" : "admin", 
                "Pass_word" : "admin",
                "Permission" : user_permissions[99],
                "Other info" : "The user with full acess"
            }
        adm_card = {}
        adm_card[0] = card 
        create_new_base(adm_card,path)

def chek_foloder(path):
    if not os.path.exists(path):
        create_a_base(path)


def creation_folder(user_card:dict , name_of_file : str):
    for key,item in user_card.items():
        path = f'Data_base/{key}_{item["User_Name"]}'
        if not os.path.exists(path):
            os.makedirs(path)
        path += f"/{key}_{item['User_Name']}_{name_of_file}_list.json"
        chek_foloder(path)

def foloder_for_new_user_creation(user_card : dict):
    creation_folder(user_card , type_of_files_dict[1])
    creation_folder(user_card , type_of_files_dict[2])
    creation_folder(user_card , type_of_files_dict[3])
    creation_folder(user_card , type_of_files_dict[4])
        
