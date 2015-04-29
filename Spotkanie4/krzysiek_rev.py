def rev(my_list):
    if my_list:
        if len(my_list) > 1:
            my_list[-1], my_list[0] = my_list[0], my_list[-1]
            temp = rev(my_list[1:-1])
            temp.insert(0, my_list[0])
            temp.append(my_list[-1])
            return temp
        else:
            return my_list
    else:
        return my_list
