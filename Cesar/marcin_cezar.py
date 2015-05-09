secret_message = """Vjg Bgp qh Ravjqp

Dgcwvkhwn ku dgvvgt vjcp wina.

Gzrnkekv ku dgvvgt vjcp kornkekv.

Ukorng ku dgvvgt vjcp eqorngz.

Eqorngz ku dgvvgt vjcp eqornkecvgf.

Hncv ku dgvvgt vjcp pguvgf.

Urctug ku dgvvgt vjcp fgpug.

Tgcfcdknkva eqwpvu.

Urgekcn ecugu ctgp'v urgekcn gpqwij vq dtgcm vjg twngu.

Cnvjqwij rtcevkecnkva dgcvu rwtkva.

Gttqtu ujqwnf pgxgt rcuu ukngpvna.

Wpnguu gzrnkekvna ukngpegf.

Kp vjg hceg qh codkiwkva, tghwug vjg vgorvcvkqp vq iwguu.

Vjgtg ujqwnf dg qpg - cpf rtghgtcdna qpna qpg - qdxkqwu yca vq fq kv.

Cnvjqwij vjcv yca oca pqv dg qdxkqwu cv hktuv wpnguu aqw'tg Fwvej.

Pqy ku dgvvgt vjcp pgxgt.

Cnvjqwij pgxgt ku qhvgp dgvvgt vjcp tkijv pqy.

Kh vjg korngogpvcvkqp ku jctf vq gzrnckp, kv'u c dcf kfgc.

Kh vjg korngogpvcvkqp ku gcua vq gzrnckp, kv oca dg c iqqf kfgc.

Pcogurcegu ctg qpg jqpmkpi itgcv kfgc - ngv'u fq oqtg qh vjqug!"""


def decodeline(code, shift):
    message = ''
    for iter in range(len(code)):
        if code[iter] in 'abcdefghijklmnopqrstuvwxyz':
            position = (ord(code[iter]) + shift - 97) % 26
            message += chr(97 + position)
        else:
            message += code[iter]
    return message

def decode_message(code, n):
    decoded = 'DECODED MESSAGE:\n\n'
    for row in code.lower().split('\n'):
        decoded += decodeline(row, n) + '\n'
    print(decoded)

decode_message(secret_message, 24)
