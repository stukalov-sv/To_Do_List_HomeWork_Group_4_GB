import json

def take_from_base(path):
    with open(path, 'r') as infile:
        data = json.load(infile)
        infile.close()
    return data

def rewrite_base(dictionary,path):
    with open(path, 'w') as outfile:
        json.dump(dictionary, outfile,indent=2)
        outfile.close()

def create_a_base(path):
    file = open(path , 'w')
    file.close()

