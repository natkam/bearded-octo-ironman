def decrypt_n(text, n=3):
    text = text.upper()
    result = ''
    for i in range(len(text)):
        if text[i] in list(string.ascii_uppercase):
            result += ''.join(chr((65 + (ord(text[i]) - (39 + n)) % 26)))
        elif text[i] == ' ':
            result += ''.join(text[i])
        else:
            result += ''.join(text[i])
    return result

txt = 'tekst.txt'

with open(txt, 'r') as f:
    for line in f:
        print(decrypt_n(line.rstrip(), n=2))