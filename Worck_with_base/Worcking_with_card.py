def change(data : dict , what_to_change: str , new_info : str,id_were_to_change : int) ->dict:
    data[id_were_to_change][what_to_change] = new_info
    return data

def delete_card(id_card : int , base : dict) -> dict:
    delete = base.pop(id_card)
    print(delete)
    return delete

