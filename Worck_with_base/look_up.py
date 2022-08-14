def look_up_by_date(date,base):
    return dict(filter(lambda x : x[1]["Time_to_do"] ==  date, base.items()))
def look_up_by_type(type,base):
    return dict(filter(lambda x : x[1]["Type_of_card"] ==  type, base.items()))
def look_up_by_name(type,base):
    return dict(filter(lambda x : x[1]["Name"] ==  type, base.items()))
