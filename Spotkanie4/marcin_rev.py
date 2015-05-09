def rev(my_list):
    len_list = len(my_list)
    if len_list > 1:
        first_elem = my_list[0]
        tmp_list = rev(my_list[1:])
        tmp_list.append(first_elem)
        return tmp_list
    elif len_list == 0:
        return [] 
    else:
        return [my_list[-1]]

if __name__ == '__main__':
    print("Test 1, my_list=[]       , rev(my_list)=" + str(rev([])))
    print("Test 2, my_list=[1,2,3,4], rev(my_list)=" + str(rev([1,2,3,4])))
    print("Test 3, my_list=[5,5,5,5], rev(my_list)=" + str(rev([5,5,5,5])))

