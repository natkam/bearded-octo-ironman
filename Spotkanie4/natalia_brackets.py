nawiasy1 = "{([])}()[{}{}]{[]}"
nawiasy2 = "()[{}{}]"
nawiasy3 = "{[}]"

otwarte = ["(", "[", "{"]
zamkniete = [")", "]", "}"]

def match(a, b):
	# if a=="(" and b==")":
	# 	return True
	# elif a=="[" and b=="]":
	# 	return True
	# elif a=="{" and b=="}":
	# 	return True
	if (abs(ord(a)-ord(b))<=2) and (a<b):
		return True
	else:
		return False

tmp_list = []

def foo(nawiasy):
	for nawias in nawiasy:
		if nawias in otwarte:
			tmp_list.append(nawias)
		elif  len(tmp_list)>0 and match(tmp_list[len(tmp_list)-1], nawias): 
			tmp_list.pop()
		else:
			print("blednie sparowane nawiasy")
			return False

	if len(tmp_list)>0:
		print("blednie sparowane nawiasy")
		return False
	else:
		print("poprawnie sparowane nawiasy")
		return True

foo(nawiasy1)
print(tmp_list) # powinna byc pusta, jesli poprawnie sparowane
