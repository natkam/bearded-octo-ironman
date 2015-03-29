import sys
from itertools import count


def custom_enumerate(list_to_enumerate, start=0):
    return zip(count(start), list_to_enumerate)


if __name__ == '__main__':
    print(custom_enumerate(sys.argv[1]), sys.argv[2])