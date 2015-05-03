book = {}

def add_phone_nr(surname, name, phone):
    book.setdefault(surname,{})
    book[surname].setdefault(name, []).append(phone)

def clean_book():
    global book
    book = {}

def search(surname):
    counter = 0
    def phone_numbers(surn):
        for phone_list in book[surn].values():
            for phone_nr in phone_list:
                yield phone_nr
    if surname in book.keys():
        for item in phone_numbers(surname):
            counter+=1
            print(item[0:3]+'-'+item[3:6]+'-'+item[6:9])
        print(counter)
    else:
        print("Surname {0} is not in the phone book.".format(surname))

if __name__ == '__main__':
    print("\nPhone book is open!")
    while True:
        print("\nChoose option:")
        option = input("A - add phone number, C - clear phone book, S - search surname, Q - quit:").upper()
        if option == 'A':
            try:
                surname, name = input("Enter surname and name (separated by spaces): ").split()
                phone = input("Enter phone number: ")
            except ValueError:
                print("Error - Remember to enter all information")
                continue
            add_phone_nr(surname.capitalize(), name.capitalize(), phone)
        elif option == 'S':
            search(input("Enter surname: ").capitalize())
        elif option == 'C':
            clean_book()
            print("Phone book is empty!")
        elif option == 'Q':
            break
        else:
            print("Your choice is incorrect!")
            continue
    print("\nThank you!\n")
