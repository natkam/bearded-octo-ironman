from os import path, listdir


def list_files(directory, level=0):
    for i in listdir(directory):
        item = path.join(directory, i)
        if path.isdir(item):
            print(level*'\t' + i + '/')
            list_files(item, level+1)
        else:
            print(level*'\t' + i)


if __name__ == '__main__':
    root_folder = '/home'
    list_files(root_folder)
