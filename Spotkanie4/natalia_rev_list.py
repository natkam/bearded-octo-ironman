'''Napisać funkcję, która rekurencyjnie odwróci listę
my_list = [1, 2, 3, 4]
rev(my_list)  => [4,3,2,1]
czyli standard, ale niech rekurencja się w  bebechach pojawi ;)
'''

my_list1 = [1, 2, "a", 17, 4]

# def rev(my_list):
# 	rev_list = []
# 	while len(my_list)>0 :
# 		rev_list.append(my_list.pop())
# 	print(rev_list)


rev_list = []

def rev(my_list):
	rev_list.append(my_list.pop())
	print(rev_list, my_list)
	if len(my_list)>0:
		rev(my_list)

rev(my_list1)


