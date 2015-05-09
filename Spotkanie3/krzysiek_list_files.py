import sys
import os

def list_files_with_walk(directory):
    return(os.walk(directory))
    
def list_files_with_recution(directory, deep=0):
    for i in os.listdir(directory):
        item = os.path.join(directory, i)
        if os.path.isdir(item):
            print (deep*'\t'+i+'/')
            list_files_with_recution(item, deep+1)
        else:
            print(deep*'\t '+ i)
        
    
if __name__ == "__main__":
    for root, dirs, files in (list_files_with_walk(str(sys.argv[1]))):
        print(root)
        for file in files:
            print('\t%s'%file)
    
    list_files_with_recution(str(sys.argv[1]))
