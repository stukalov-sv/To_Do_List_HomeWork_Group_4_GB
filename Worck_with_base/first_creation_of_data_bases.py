import json
import os
from Dictionaris import user_permissions

def take_from_base(path):
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
    return data

def rewrite_base(dictionary,path):
    with open(path, 'w') as outfile:
        json.dump(dictionary, outfile,indent=2)
        outfile.close()

def create_a_base(path):
    file = open(path , 'w')
    file.close()

def chek_for_user_base(path):
    if not os.path.exists(path):
        create_a_base(path)
        adm_card = \
            {
                "User_ID" : 0 ,
                "User_Name" : "admin", 
                "Pass_word" : "admin",
                "Permission" : user_permissions[99],
                "Other info" : "The user with full acess"
            }
        rewrite_base(adm_card,path)