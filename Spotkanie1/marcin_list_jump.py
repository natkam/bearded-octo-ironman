def fun(L):
    index = 0
    set_ind = set()
    len_L = len(L)
    while unify_ind(index, len_L) not in set_ind:
        if  -len(L) <= index < len(L):
            set_ind.add(index)
            index = index + L[index]
        else:
            return len(set_ind)
    return -1

def unify_ind(ind, tab_len):
    return ind + tab_len if ind < 0 else ind

if __name__ == '__main__':
    test_1 = [-1 for i in range(10)]
    test_2 = [1 for i in range(10)]
    test_3 = [0]
    test_4 = [2,3,-1,1,3]
    test_5 = [1,-3,5,1]

    print("Test 1: {0}".format(fun(test_1) == -1))
    print("Test 2: {0}".format(fun(test_2) == 10))
    print("Test 3: {0}".format(fun(test_3) == -1))
    print("Test 4: {0}".format(fun(test_4) == 4))
    print("Test 5: {0}".format(fun(test_5) == 4))
