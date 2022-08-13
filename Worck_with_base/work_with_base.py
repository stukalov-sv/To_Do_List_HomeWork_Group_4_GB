from email.mime import base
import json

def rewrite_base_with_index_append(dictionary_to_add : dict,path : str):
    dictionary_were_to_add = {}
    try:
        dictionary_were_to_add = take_from_base(path)
        dictionary_were_to_add[int(max(dictionary_were_to_add.keys()))+1] = dictionary_to_add
    except:
        dictionary_were_to_add[0] = dictionary_to_add
    with open(path, 'w') as outfile:
        json.dump(dictionary_were_to_add, outfile,indent=2)
        outfile.close()

def rewrite_base(dictionary_to_rewrite : dict,path : str):
    with open(path, 'w') as outfile:
        json.dump(dictionary_to_rewrite, outfile,indent=2)
        outfile.close()

def take_from_base(path) -> dict:
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
    return data

def copy_to_other_base(data_card:dict, path_to:str, id_card : int):
    # base_to_rewrite = {}
    data_new = {}
    try:
        base_to_rewrite = take_from_base(path_to)
    except:
        base_to_rewrite = {}
    for item in data_card.values():
        if type(item) == dict:
            data_new = dict(item.items())
    print(id_card,data_card,data_new)
    base_to_rewrite[id_card] = data_new
    return base_to_rewrite

def delete_element_by_id(base_from : dict , id_card : int):
    # print(id_card,base_from)
    # x = base_from.pop(id_card)
    try:
        del base_from[str(id_card)]
    except:
        print(f"No task with ID {id_card}")
    return base_from

# [meal.pop(key) for key in ['fats', 'proteins']]

def move_from_active_to_complete(base_active : dict , base_complete : dict , id_card):
    data = base_active.pop(id_card)
    base_complete[id_card] = data
    return base_active,base_complete

def rewrite_info_from_full(data_what_to_rewrite : dict , data_full : dict ):
    new_dict = {}
    for key in data_what_to_rewrite.keys():
        print(key,data_full[key])
        new_dict[key] = data_full[key]
    return new_dict


# def list_of_things(name_of_fiels,data):
