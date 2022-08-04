from tkinter import *
from unicodedata import name
# from tkinter import ttk
# import Dictionaris as dct

global name_to_use
global pass_to_use

def user_access():
    def clicked_ok():
        txt_log.get()
        txt_pass.get()
        window.destroy()
        # global name_to_use
        # name_to_use = txt_log.get()
        # global pass_to_use
        # pass_to_use = txt_pass.get()
        # return txt_log.get(),txt_pass.get()


    def clicked_canc():
        print("Cancel")
        window.destroy()


    def clicked_create():
        print("Create new user")
        window.destroy()

    # global pass_to_use
    # pass_to_use = ""
    # global name_to_use
    # name_to_use = ""

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
    # print(txt_log.get(),txt_pass.get())
    window.mainloop()
    # return clicked_ok()



def card_create(dict_of_rows: dict):
    def clicked_ok():
        print(txt_name.get())
        print(combo_toc.get())
        print(txt_comm.get())
        print(txt_ttd.get())
        print(txt_ctime.get())
        window.destroy()

    def clicked_canc():
        print("Cancel")
        window.destroy()

    window = Tk()
    window.title("Создание карточки")


    for i, j in dict_of_rows.items():
        Message(window, width=350, text=j) \
                .grid(row=i, column=0, sticky=W)


    txt_name = Entry(window, width=22)
    txt_name.grid(column=1, row=1)
    combo_toc = ttk.Combobox(window,
                                values=[
                                    "background",
                                    "in_work",
                                    "done",
                                    "deleted"])
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
    
def colums_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')  

    new_list = []
    new_list_index = []
    print (data.items())
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


tel_row = \
    {
        1 : "Name" ,
        2 : "Type_of_card" ,
        3 : "Comment",
        4 : "Time_to_do",
        5 : "Create_time"
    }

data = {
    "0": {
      "Name": "Igor",
      "Type_of_card": "Penschii",
      "Comment": "male",
      "Time_to_do": "friend",
      "Create_time": "+ 373 68 032305"
    },
    "1": {
      "Name": "Artiom",
      "Type_of_card": "S",
      "Comment": "male",
      "Time_to_do": "family",
      "Create_time": "+ 373 68 482305"
    },
    "2": {
      "Name": "Oleg",
      "Type_of_card": "S",
      "Comment": "male",
      "Time_to_do": "tovarish",
      "Create_time": "+ 373 78 482305"
    },
    "3": {
      "Name": "Liza",
      "Type_of_card": "S",
      "Comment": "female",
      "Time_to_do": "person",
      "Create_time": "+ 373 78 482305"
    },
    "4": {
      "Name": "Kira",
      "Type_of_card": "S",
      "Comment": "female",
      "Time_to_do": "family",
      "Create_time": "+ 373 78 482305"
    },
    "6": {
      "Name": "Liza",
      "Type_of_card": "S",
      "Comment": "female",
      "Time_to_do": "family",
      "Create_time": "+ 373 78 482305"
    }
  }

# user_access()
# card_create(dct.cards_dictionary.card_id_dict)
# colums_output(tel_row, data)

