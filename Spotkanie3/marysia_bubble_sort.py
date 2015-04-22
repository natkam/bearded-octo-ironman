
def bubble_sort(list_to_sort):
    is_sorted = False
    n = len(list_to_sort) - 1
    while not is_sorted:
        is_sorted = True

        for i in range(n):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                is_sorted = False
            print(list_to_sort)
        n -= 1
    return list_to_sort


if __name__ == '__main__':
    list_to_sort = [90, 2, 9, 4, 1, 34]
    bubble_sort(list_to_sort)
