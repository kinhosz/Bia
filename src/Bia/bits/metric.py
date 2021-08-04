from datetime import datetime

dict = {}

def metric(name, start):

    global dict

    if start:
        dict[name] = datetime.now()
    else:
        if name not in dict.keys():
            print("not registered")
        else:
            curr = datetime.now()
            past = dict[name]

            delta = curr - past
            print("elapsed =", delta.total_seconds(), name)