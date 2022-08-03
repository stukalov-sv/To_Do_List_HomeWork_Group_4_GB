import json

def rewrite_base_with_index_append(dictionary_to_add : dict,path : str):
    dictionary_were_to_add = take_from_base(path)
    dictionary_were_to_add[int(max(dictionary_were_to_add.keys()))+1] = dictionary_to_add
    with open(path, 'w') as outfile:
        json.dump(dictionary_were_to_add, outfile,indent=2)
        outfile.close()

def take_from_base(path) -> dict:
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
    return data

def copy_to_other_base(base_from : dict , base_to :dict , id_card : int):
    base_to[id_card] = base_from[id_card]
    return base_from

def delete_element_by_id(base_from : dict , id_card : int):
    base_from.pop(id_card)
    return base_from

def move_from_active_to_complete(base_active : dict , base_complete : dict , id_card):
    data = base_active.pop(id_card)
    base_complete[id_card] = data
    return base_active,base_complete