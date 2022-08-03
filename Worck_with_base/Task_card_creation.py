import datetime
from Dictionaris import card_type

def create_a_tas_kard(card_name = "Test",type_of_card = 6,comment = "For testing purp",time_to_do = datetime.datetime(2022,8,4,17)) -> dict:

    
    card = \
        {
            "Name" : card_name ,
            "Type_of_card" : card_type[type_of_card] ,
            "Comment" : comment ,
            "Time_to_do" : time_to_do ,
            "Created_time" : datetime.datetime.now()
        }
    
    # print(card)
    return card

def path_creation_for_user_base(id_user : int ,type_of_base:int,data : dict) -> str:
    return f"Data_base/{id_user}_{data[id_user]['User_Name']}/{id_user}_{data[id_user]['User_Name']}_{type_of_files_dict[type_of_base]}_list.json"