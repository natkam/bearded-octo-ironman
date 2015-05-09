
my_directory = {}


def add_number():
    print("Enter name, surname and a phone number")
    while True:
        try:
            name, surname, tel = input("> ").split()
            break
        except ValueError:
            print("name, surname and phone number, please")

    my_directory.setdefault(surname, {}).setdefault(name, []).append(tel)
    print("A new number has been added successfully")


def clear_directory():
    global my_directory
    my_directory = {}


def numbers_for_surname():
    print("Enter the surname:")
    surname_entry = my_directory[input("> ")]

    def get_phones():
        for j in surname_entry:
            for k in surname_entry[j]:
                yield k

    print("Numbers:")
    counter = 0
    for i in get_phones():
        print(i)
        counter += 1
    print(counter)


while True:
    print("""\nWelcome to the phone directory service!
Enter:
\tadd - to add a new number
\tclear - to clear the directory
\tnumbers - list numbers for a surname""")
    operation = input("> ").lower()
    if operation == "add":
        add_number()
    elif operation == "clear":
        clear_directory()
    elif operation == "numbers":
        numbers_for_surname()
    else:
        print("Command nor recognized")
    print("\n" + str(my_directory))

