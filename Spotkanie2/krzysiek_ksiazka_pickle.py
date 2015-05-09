import pickle
import os.path


def phonebook_pickle(func):
    global phonebook
    def wraper(*args, **kwargs):
        with open('phonebook_data.pkl', 'wb') as database:
            func(*args, **kwargs)
            pickle.dump(phonebook, database)
    return wraper

def init():
    global phonebook
    if not os.path.exists('phonebook_data.pkl'):
        database = open('phonebook_data.pkl', 'wb')
        phonebook = {}
        pickle.dump(phonebook, database)
        database.close()
    else:
        database = open('phonebook_data.pkl', 'rb')
        phonebook = pickle.load(database)

@phonebook_pickle
def add_number(name,lastname,number):
    global phonebook
    phonebook.setdefault(lastname, {})
    phonebook[lastname].setdefault(name,[]).append(number)

@phonebook_pickle    
def clean():
    global phonebook
    phonebook.clear()

def search(lastname):
    global phonebook
    #counter = 0
    try:
        for name in phonebook[lastname]:
            for number in phonebook[lastname][name]:
                yield number
                #counter +=1
        #yield counter
    except KeyError:
        return("There is no such lastname as %s, maybe add him first?"% lastname)
        raise StopIteration("There is no such lastname as %s, maybe add him first?"% lastname)


         
if __name__ == '__main__':
    init()
    while True:
        decision = input("What you want to do >> ")
        if decision == 'add':
            data = input("Please provide name, lastname and number >> ")
            add_number(data.split()[0],data.split()[1],data.split()[2])
        elif decision == 'clean':
            clean()
            print("You purge your phonebook. Congrats")
        elif decision == 'search':
            data = input("Please provide lastname >> ")
            for number in search(data):
                print (number)
            print(sum(1 for i in search(data)))
        elif decision == 'exit':
            break
