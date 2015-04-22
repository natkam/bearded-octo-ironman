import pickle


def flatten(nested_item):
    flatten_list = []
    if isinstance(nested_item, list):
        for i in nested_item:
            flatten_list += flatten(i)
    elif isinstance(nested_item, dict):
        for i, j in nested_item.items():
            flatten_list += flatten(j)
    else:
        flatten_list.append(nested_item)

    return flatten_list


def flatten_file(file):
    pickle_file = open(file, 'rb')
    items = pickle.load(pickle_file)
    pickle_file.close()
    return flatten(items)


if __name__ == '__main__':
    print(flatten_file('marysia_pickle_jar'))
