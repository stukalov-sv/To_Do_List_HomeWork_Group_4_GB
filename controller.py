import Worck_with_base as WWB
from constants import user_data_base_path

def  chekin():
    Name = input("Представьтесь : ")
    Password = input("Ваш пароль : ")
    User_ID,User_Name,User_status = WWB.User_chek(Name,Password,WWB.take_from_base(user_data_base_path))
    path_full = WWB.path_creation_for_user_base(User_ID,1,user_data_base_path)
    path_active = WWB.path_creation_for_user_base(User_ID,2,user_data_base_path)
    path_done = WWB.path_creation_for_user_base(User_ID,3,user_data_base_path)
    path_deleted = WWB.path_creation_for_user_base(User_ID,4,user_data_base_path)

def bases_check():
    WWB.chek_for_user_base(user_data_base_path)
    WWB.foloder_for_new_user_creation(WWB.take_from_base(user_data_base_path))

def adm_button():
    WWB.rewrite_base_with_index_append(WWB.create_a_user(WWB.take_from_base(user_data_base_path)),user_data_base_path)

def user_button():
    WWB.rewrite_base_with_index_append(WWB.create_a_user(WWB.take_from_base(user_data_base_path)),user_data_base_path)



# WWB.create_a_tas_kard()
