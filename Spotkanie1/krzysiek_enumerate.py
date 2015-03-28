from itertools import count

def enum(iterable, start=0):
    return zip(count(start), iterable)
    
   
if __name__ == '__main__':
    test = "testingstring"
    for i in enum(test):
        print(i) 
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enum(seasons)))
