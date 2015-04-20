import pickle

def flatten(elem_nested):
    all_flatten = tuple()
    if isinstance(elem_nested, list):
        for item in elem_nested:
            all_flatten += flatten(item)
    elif isinstance(elem_nested, tuple):
        for item in elem_nested:
            all_flatten += flatten(item)
    elif isinstance(elem_nested, dict):
        for val in elem_nested.values():
            all_flatten += flatten(val)
    else:
        all_flatten += (elem_nested,)
    return all_flatten

if __name__ == '__main__':
    obj = open('marcin_file.pickle', 'rb')
    pickle_obj = pickle.load(obj)
    print(flatten(pickle_obj))
    obj.close()
