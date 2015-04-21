import pickle

def flatten(obj):
    flatten_objects = []
    if isinstance(obj, list):
        for i in obj:
            flatten_objects += flatten(i)
    elif isinstance(obj, dict):
        for k,v in obj.items():
            flatten_objects += flatten(k)
    else:
        flatten_objects.append(obj)
    return flatten_objects
            
if __name__ == '__main__':
    file = open('pickle.txt', 'rb')
    obj = pickle.load(file)
    print(flatten(obj))


