import datetime
import os


def logger(string: str):
    time = datetime.datetime.today()
    print(time)
    res_str = str(time) + ' | ' + string
    print(res_str)
    with open(path, 'a') as writer:
        writer.write(res_str + '\n')


path = os.path.join('Logs', 'logs.csv')

# logger('hello')