def valid_brackets(bracket_string):
    if not bracket_string:
        return False
    brackets = {'left':'([<{', 'right':')]>}','pairs':('[]', '{}', '()', '<>')}
    tmp_table = []
    for last in bracket_string:
        if last in brackets['left'] :
            tmp_table.append(last)
        elif last in brackets['right']:
            if not tmp_table:
                return False
            left_in_pair = tmp_table.pop()
            if (left_in_pair + last) not in brackets['pairs']:
                return False
        else:
            return False
    return not tmp_table

if __name__ == '__main__':
    print("False is OK, test_1 = ",valid_brackets(''))
    print("False is OK, test_2 = ",valid_brackets('[}'))
    print("False is OK, test_3 = ",valid_brackets('{'))
    print("True  is OK, test_4 = ",valid_brackets('{[](<>)}'))
    print("False is OK, test_5 = ",valid_brackets('abc'))
