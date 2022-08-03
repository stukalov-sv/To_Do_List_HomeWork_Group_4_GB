from tkinter import *
  
def user_access():
    def clicked_ok():
        print(txt_log.get())
        print(txt_pass.get())


    def clicked_canc():
        print("Cancel")
        window.destroy()

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
    window.mainloop()

    
def colums_output(dict_of_rows : dict , data : dict):
    window = Tk()
    window.title('Информационная карточка')  

    new_list =[]
    new_list_index =[]
    for i,item in data.items():
        if type(item) == dict:
            data_new = dict(item.items())
        new_list.append(data_new)
        new_list_index.append(i)
    print(new_list)
    print(new_list_index)

    card_frame_0 = LabelFrame(window, text='ID')
    card_frame_0.grid(row=0, column=0)
    for i,j in dict_of_rows.items():
        Message(card_frame_0, width=350, text=j) \
                .grid(row=i, column=0, sticky=W)
    
    for y in range(len(new_list)):
        card_frame = LabelFrame(window, text=f'{new_list_index[y]}')
        card_frame.grid(row=0, column=y+1)
        row_count = 0
        for i,j in new_list[y].items():          
            Message(card_frame, width=300, text=j) \
                    .grid(row=row_count+1, column=y+1)
            row_count += 1

        print(1)

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


user_access()
colums_output(tel_row, data)

