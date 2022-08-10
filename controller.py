import Worck_with_base as WWB
import Dictionaris as Dic
from Worck_with_base.work_with_base import rewrite_info_from_full, take_from_base
from constants import user_data_base_path
import data_in_out as IO_M
import interface as UI






def bases_check():
    WWB.chek_for_user_base(user_data_base_path)
    WWB.foloder_for_new_user_creation(WWB.take_from_base(user_data_base_path))


def user_button():
    WWB.rewrite_base_with_index_append(WWB.create_a_user(WWB.take_from_base(user_data_base_path)),user_data_base_path)

def  chekin():

    check_bool = True
    button = 1

    while check_bool and button == 1:
        Name,Password,button =IO_M.user_access()
        User_ID,User_Name,User_status = WWB.User_chek(Name,Password,WWB.take_from_base(user_data_base_path))
        print(User_ID,User_Name,User_status)
        if User_Name != None and User_status != None:
            check_bool = False

    match button:
        case 2:
            chek = True
            while chek:
                Name = input("Enter name : ")
                if WWB.User_chek_name(Name,WWB.take_from_base(user_data_base_path)) == None:
                    chek = False
            Password = input("Enter password : ")
            WWB.rewrite_base_with_index_append(WWB.create_a_user(Name,Password),user_data_base_path)
        case 3:
            path_full = None
            path_active = None
            path_done = None
            path_deleted = None
    try:
        path_full = WWB.path_creation_for_user_base(User_ID,1,WWB.take_from_base(user_data_base_path))
        path_active = WWB.path_creation_for_user_base(User_ID,2,WWB.take_from_base(user_data_base_path))
        path_done = WWB.path_creation_for_user_base(User_ID,3,WWB.take_from_base(user_data_base_path))
        path_deleted = WWB.path_creation_for_user_base(User_ID,4,WWB.take_from_base(user_data_base_path))
    except:
        print("Exiting")
    return Name,Password,User_ID,User_Name,User_status,path_full,path_active,path_done,path_deleted

def adm_button():
    UI.description()
    Name,Password,User_ID,User_Name,User_status,path_full,path_active,path_done,path_deleted = chekin()
    bases_check()
    match Name:
        case None:
            print("This program dosen't have functional for unregistated users , good bie ")
        case _:
            if Name == "admin":
                print("Hi BOSS , what's up ? ")
            else :
                print(f"Hello {Name} , nice to see you =)")
    option = UI.input_options_what_to_do()
    match option:   
        case 1:
            option_2 =UI.input_options_how_to_find()
            match option_2:
            # Поиск по дате
                case 1: 
                    for i in WWB.take_from_base(path_full).values():
                        print(i["Time_to_do"])
                    date = input("Enter date to find : ")
                    data = WWB.look_up_by_date(date,WWB.take_from_base(path_active))
            # Поиск по типу
                case 2:
                    for i in WWB.take_from_base(path_full).values():
                        print(i["Type_of_card"])
                    Type = input("Enter type to find : ")
                    data = WWB.look_up_by_type(Type,WWB.take_from_base(path_active))
            # Поиск по имени
                case 3 :
                    for i in WWB.take_from_base(path_full).values():
                        print(i["Name"])
                    name = input("Enter name to find : ")
                    data = WWB.look_up_by_name(name,WWB.take_from_base(path_active))
            
            repeat_option_2 = 1
            option_3 = UI.options_deals()
            while repeat_option_2 == 1:
                match option_3:
                    case 1:
                        IO_M.colums_output(Dic.card_id_dict,data)
                        repeat_option_2 = UI.repeat_options ()
                    case 2:
                        id_to_cange = input("ID where to change : ")
                        print("what to change : ")
                        for key,item in Dic.card_id_dict.items():
                            if key != 0:
                                print(f"{key} : {item}")
                        what_to_change = int(input("Your choise : "))
                        if what_to_change == 2:
                            for key,item in Dic.card_type.items():
                                print(f"{key} : {item}")
                            new_info = int(input("enter new info : "))
                            WWB.rewrite_base(WWB.change(WWB.take_from_base(path_full),Dic.card_id_dict[what_to_change],Dic.card_type[new_info],id_to_cange),path_full)
                            IO_M.colums_output(Dic.card_id_dict,WWB.take_from_base(path_full))
                        else:
                            new_info = input("enter new info : ")
                            WWB.rewrite_base(WWB.change(WWB.take_from_base(path_full),Dic.card_id_dict[what_to_change],new_info,id_to_cange),path_full)
                            IO_M.colums_output(Dic.card_id_dict,WWB.take_from_base(path_full))
                        try:
                            WWB.rewrite_base(rewrite_info_from_full(take_from_base(path_active),take_from_base(path_full)),path_active)
                        except:
                            print("No active task's")
                        try:
                            WWB.rewrite_base(rewrite_info_from_full(take_from_base(path_done),take_from_base(path_full)),path_done)
                        except:
                            print("No done task's")
                        try:
                            WWB.rewrite_base(rewrite_info_from_full(take_from_base(path_deleted),take_from_base(path_full)),path_deleted)
                        except:
                            print("No deleted task's")

                        repeat_option_2 = UI.repeat_options ()
                    case 3:
                        id_to_delete = int(input("ID to delete : "))
                        WWB.rewrite_base(WWB.copy_to_other_base(take_from_base(path_full),path_deleted,id_to_delete),path_deleted)
                        WWB.rewrite_base(WWB.delete_element_by_id(take_from_base(path_active),id_to_delete),path_active)
                        
                        repeat_option_2 = UI.repeat_options ()
        case 2:
            card_name,type_of_card,comment,time_to_do,x = IO_M.card_create(Dic.card_id_dict)
            WWB.rewrite_base_with_index_append(WWB.create_a_tas_kard(card_name,type_of_card,comment,time_to_do),path_full)
            WWB.rewrite_base(WWB.copy_to_other_base(WWB.take_from_base(path_full),path_active,int(max(WWB.take_from_base(path_full).keys()))),path_active)
            IO_M.colums_output(Dic.card_id_dict,WWB.take_from_base(path_full)[int(max(WWB.take_from_base(path_full).keys()))])
        # case 3:
            # Актуальный
            # Выполненный

