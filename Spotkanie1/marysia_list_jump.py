
jump_list = [2, 3, -1, 1, 3]
cycle_list = [1, 1, -2, 1]


def list_jumper(jump_list):
    i = 0
    count = 0
    index_list = []
    while True:
        try:
            if i in index_list:
                print(-1)
                break

            index_list.append(i)
            i = i + jump_list[i]
            count += 1
        except IndexError:
            print(count)
            break


list_jumper(cycle_list)