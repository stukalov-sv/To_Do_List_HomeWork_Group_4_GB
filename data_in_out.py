import os
import json
from tkinter import *
from unicodedata import name
from tkinter import ttk
import Dictionaris as dct


def user_access():
    def clicked_ok():
        global name_to_use, pass_to_use, action_num
        name_to_use = txt_log.get()
        pass_to_use = txt_pass.get()
        action_num = 1
        window.destroy()


    def clicked_canc():
        global action_num
        action_num = 3
        window.destroy()


    def clicked_create():
        global action_num
        action_num = 2
        window.destroy()

    global pass_to_use, name_to_use, action_num
    pass_to_use = None
    name_to_use = None
    action_num = None

    window = Tk()  
    window.title("Добро пожаловать")  
    window.geometry('250x150')  
    lbl_log = Label(window, text="Login")  
    lbl_log.grid(column=0, row=0)
    lbl_pass = Label(window, text="Password")
    lbl_pass.grid(column=0, row=1)
    txt_log = Entry(window,width=10) 
    txt_log.grid(column=1, row=0)
    txt_pass = Entry(window,width=10) 
    txt_pass.grid(column=1, row=1)
    lbl_log = Label(window, text="")
    lbl_log.grid(column=0, row=2)
    btn = Button(window, text="ОК", command=clicked_ok)  
    btn.grid(column=0, row=3)
    btn = Button(window, text="Cancel", command=clicked_canc)
    btn.grid(column=1, row=3)
    btn = Button(window, text="Create new user", command=clicked_create)
    btn.grid(column=2, row=3)

    window.mainloop()
    # print(name_to_use, pass_to_use, action_num)
    return name_to_use, pass_to_use, action_num


def card_create(dict_of_rows: dict):
    def clicked_ok():
        global user_name, toc, comm, ttd, ctime
        user_name = txt_name.get()
        toc = combo_toc.get()
        comm = txt_comm.get()
        ttd = txt_ttd.get()
        ctime = txt_ctime.get()
        window.destroy()

    def clicked_canc():
        print("Cancel")
        window.destroy()

    global user_name, toc, comm, ttd, ctime
    user_name = None
    toc = None
    comm = None
    ttd = None
    ctime = None

    window = Tk()
    window.title("Создание карточки")


    for i, j in dict_of_rows.items():
        Message(window, width=350, text=j) \
                .grid(row=i, column=0, sticky=W)

    type_list = list(dct.card_type.values())

    txt_name = Entry(window, width=22)
    txt_name.grid(column=1, row=1)
    combo_toc = ttk.Combobox(window,
                                values=type_list)
    combo_toc.grid(column=1, row=2)
    combo_toc.current(1)
    txt_comm = Entry(window, width=22)
    txt_comm.grid(column=1, row=3)
    txt_ttd = Entry(window, width=22)
    txt_ttd.grid(column=1, row=4)
    txt_ctime = Entry(window, width=22)
    txt_ctime.grid(column=1, row=5)
    lbl_log = Label(window, text="")
    lbl_log.grid(column=0, row=6)
    btn = Button(window, text="ОК", command=clicked_ok)
    btn.grid(column=0, row=7)
    btn = Button(window, text="Cancel", command=clicked_canc)
    btn.grid(column=1, row=7)

    window.mainloop()
    return user_name, toc, comm, ttd, ctime
    
def colums_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')  

    new_list = []
    new_list_index = []
    # print(data.items())
    for i, item in data.items():
        if type(item) == dict:
            data_new = dict(item.items())
        new_list.append(data_new)
        new_list_index.append(i)
    # print(new_list)
    # print(new_list_index)

    card_frame_0 = LabelFrame(window, text='ID')
    card_frame_0.grid(row=0, column=0)
    for i, j in dict_of_rows.items():
        Message(card_frame_0, width=350, text=j) \
                .grid(row=i, column=0, sticky=W)
    
    for y in range(len(new_list)):
        card_frame = LabelFrame(window, text=f'{new_list_index[y]}')
        card_frame.grid(row=0, column=y+1)
        row_count = 0
        for i, j in new_list[y].items():
                Message(card_frame, width=300, text=j) \
                        .grid(row=row_count+1, column=y+1)
                row_count += 1

    window.mainloop()

test_path = os.path.join('Data_base', '1_Test', '1_Test_full_list.json')

with open(test_path) as file:
    test_card = json.load(file)
    print(test_card)

# u_nam, u_pas, u_action = user_access()
# u_name, u_toc, u_comm, u_ttd, u_ctime = card_create(dct.cards_dictionary.card_id_dict)
# colums_output(dct.cards_dictionary.card_id_dict, test_card)

# print(u_nam, u_pas, u_action)
# print(u_name, u_toc, u_comm, u_ttd, u_ctime)