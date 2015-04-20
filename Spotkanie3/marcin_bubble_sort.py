def bubble_sort(tosort, how_to_sort = 'asc'):
    '''
    bubble_sort(tosort, how_to_sort='asc') --> new sorted list

    tosort is a list, how_to_sort is a string in ('asc', 'desc')

    >>> bubble_sort([3, 2, 1])
    [1, 2, 3]
    >>> bubble_sort([4, 5, 6],'desc')
    [6, 5, 4]
    >>> bubble_sort([7, 7, 7])
    [7, 7, 7]
    '''
    tosort = list(tosort)
    issorted, list_len = 0, len(tosort)
    if how_to_sort == 'asc':
        while issorted < list_len:
            issorted = 1
            for item in range(1, list_len):
                if tosort[item-1] > tosort[item]:
                    tosort[item-1], tosort[item] = tosort[item], tosort[item-1]
                else:
                    issorted += 1
        return tosort
    elif how_to_sort == 'desc':
        while issorted < list_len:
            issorted = 1
            for item in range(1, list_len):
                if tosort[item-1] < tosort[item]:
                    tosort[item-1], tosort[item] = tosort[item], tosort[item-1]
                else:
                    issorted += 1
        return tosort
    else:
        print("Error, how_to_sort can be one 'asc' or 'desc'")
        return []

if __name__ == "__main__":
    import doctest
    doctest.testmod()