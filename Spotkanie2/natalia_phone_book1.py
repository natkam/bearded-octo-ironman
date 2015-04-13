# Ksiazka telefoniczna - bez sortowania alfabetycznego

import itertools

phone_book = {}


def add_contact(surname, name, phone):
	if surname in phone_book:
		if name in phone_book[surname]:
			if phone in phone_book[surname][name]:
				print("Ten numer jest juz dodany.")
			else:
				phone_book[surname][name].append(phone)
		else:
			new_name = dict.fromkeys([name], [phone])
			phone_book[surname].update(new_name)
	else:
		ph1 = dict.fromkeys([name], [phone])
		con1 = dict.fromkeys([surname], ph1)
		phone_book.update(con1)
	return



def number_gen(surname, name):
	for i in itertools.count():
		if i >= len(phone_book[surname][name]):
			print(i)
			break
		yield phone_book[surname][name][i]
		# issue: jesli do danej osoby nie przypisze sie zadnego nru, fcja "number_gen" wypisuje i = 1 (tzn. tablica nrow ma len==1)


def show_contact():
	surname = input("Podaj nazwisko: ")
	if surname in phone_book:
		names = list(phone_book[surname].keys())
		if len(phone_book[surname]) == 1:
			print(surname, names[0])
			for number in number_gen(surname, names[0]):
				print(number)
		else:
			print(surname, names)
			name = input("Podaj imie: ")
			if name in phone_book[surname]:
				print(surname, name)
				for number in number_gen(surname, name):
					print(number)
			else:
				print("Nie ma takiej osoby.")
	else:
		print("Nie ma takiej osoby.")
	return



print(" * * * Ksiazka telefoniczna * * * \nDostepne komendy: \n add - dodaj nowy kontakt \n show - pokaz dany kontakt \n clear - wyczysc cala ksiazke telefoniczna \n q - wyjdz z programu")

# ## tmp:
# add_contact('Asdf', 'Ada', 112)
# add_contact('Asdf', 'Ada', 113)
# add_contact('Asdf', 'Ada', 114)
# add_contact('Asdf', 'Adam', 997)
# add_contact('Smith', 'John', 998)
# add_contact('Smith', 'John', 999)
# add_contact('Blabla', 'Ala', 508)
# print("phone_book:", str(phone_book))
# ## end tmp

while True:
	dec = input("Komenda >> ")
	
	if dec == 'add':
		# issue: zadbac, by nie przyjmowalo pustych nazwisk, imion i nrow (por. komentarz przy number_gen())
		surname = input("Podaj nazwisko: ")
		name = input("Podaj imie: ")
		phone = input("Podaj telefon: ")
		# dlaczego ponizsza linia chce dokladnie 3 znakow, a nie 3 stringow?
		#surname, name, phone = input("Podaj dane: ")

		add_contact(surname, name, phone)


	elif dec == 'show':
		show_contact()
	

	elif dec == 'clear':
		sure = input("To polecenie usuwa wszystkie kontakty. Jestes pewien? (y/n) ")
		if sure == 'y':
			phone_book.clear()
			print("Pusta ksiazka telefoniczna.")
		else:
			print("Kontakty zachowane.")


	elif dec == 'q':
		break


	else:
		print("Nie ma takiej komendy.")
