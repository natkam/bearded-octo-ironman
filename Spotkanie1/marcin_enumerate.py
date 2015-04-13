from itertools import count

def my_enumerate(iterable, start=0):
    return zip(count(start), iterable)

# for no, item in my_enumerate(['a', 'b', 'c', 'd', 'e'],3):
#     print(no, item)
