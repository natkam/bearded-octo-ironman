def valid_brackets(braces_to_pair):
    braces = {'l':'([{<', 'r':')]}>'}
    temp = []
    for item in braces_to_pair:
        if item in braces['l']:
            temp.append(item)
        elif item in braces['r']:
            if temp:
                if not ((temp.pop() + item) in ('{}', '[]', '{}', '<>', '()')):
                    return False
            else:
                return False
    return True if not temp else False
