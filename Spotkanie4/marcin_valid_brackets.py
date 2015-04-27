def valid_brackets(bracket_string):
    brackets = {'left':'([<{', 'right':')]>}','pairs':('[]', '{}', '()', '<>')}
    tmp_table = []
    if len(bracket_string) == 0:
        return False
    else:
        for last in bracket_string:
            if last in brackets['left'] :
                tmp_table.append(last)
            elif last in brackets['right']:                        
                if len(tmp_table) != 0:
                    left_in_pair = tmp_table.pop()
                    if not ((left_in_pair + last) in brackets['pairs']):
                        return False
                else :
                      return False
            else :
                return False
        return True if len(tmp_table) == 0 else False

if __name__ == '__main__':
    print("False is OK, test_1 = ",valid_brackets(''))
    print("False is OK, test_2 = ",valid_brackets('[}'))
    print("False is OK, test_3 = ",valid_brackets('{'))
    print("True  is OK, test_4 = ",valid_brackets('{[](<>)}'))
    print("False is OK, test_5 = ",valid_brackets('abc'))
