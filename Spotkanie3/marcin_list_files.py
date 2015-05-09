import os, sys

def list_files(catalog_path, indent = 0):
    files_list = os.listdir(catalog_path)
    for file in files_list:
        subdir = os.path.join(catalog_path,file)
        if os.path.isdir(subdir):
            print("{0}{1}/".format(indent*' ', file))
            list_files(subdir, indent+4)
        else:
            print("{0}{1}".format(indent*' ',file))

if __name__ == '__main__':
    if os.path.isdir(sys.argv[1]):
        print("Directory tree for:", sys.argv[1])
        print("{0}/".format(os.path.basename(sys.argv[1])))
        list_files(sys.argv[1],4)
    else:
        print("Error - {} is incorrect".format(sys.argv[1]))
