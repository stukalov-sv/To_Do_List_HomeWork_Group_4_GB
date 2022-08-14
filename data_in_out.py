import os
import json
from tkinter import *
from unicodedata import name
from tkinter import ttk
import Dictionaris as dct
    
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