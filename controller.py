import Worck_with_base as WWB
import Dictionaris as Dic
from constants import user_data_base_path
import data_in_out as IO_M
import interface as UI





def bases_check():
    WWB.chek_for_user_base(user_data_base_path)
    WWB.foloder_for_new_user_creation(WWB.take_from_base(user_data_base_path))


def user_button():
    WWB.rewrite_base_with_index_append(WWB.create_a_user(WWB.take_from_base(user_data_base_path)),user_data_base_path)

def  chekin():
    IO_M.user_access()
    
    Name = input("Name : ")

    Password = input("Pass : ")

    User_ID,User_Name,User_status = WWB.User_chek(Name,Password,WWB.take_from_base(user_data_base_path))
    path_full = WWB.path_creation_for_user_base(User_ID,1,WWB.take_from_base(user_data_base_path))
    path_active = WWB.path_creation_for_user_base(User_ID,2,WWB.take_from_base(user_data_base_path))
    path_done = WWB.path_creation_for_user_base(User_ID,3,WWB.take_from_base(user_data_base_path))
    path_deleted = WWB.path_creation_for_user_base(User_ID,4,WWB.take_from_base(user_data_base_path))
    return Name,Password,User_ID,User_Name,User_status,path_full,path_active,path_done,path_deleted

def adm_button():
    UI.description()
    Name,Password,User_ID,User_Name,User_status,path_full,path_active,path_done,path_deleted = chekin()
    bases_check()
    print(f"Hi ,{Name} you have {User_status} permission")

    

# WWB.create_a_tas_kard()
