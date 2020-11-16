# -*- coding: utf-8 -*-
import hashlib


def get_min(key):
    min = '99999'
    for n in range(99999999):
        var = str(n)
        md5 = hashlib.md5()
        md5.update(key.encode('utf-8'))
        md5.update(var.encode('utf-8'))
        if md5.hexdigest() < min:
            min = md5.hexdigest()
            if min[:6] == '000000':
                break

    return n, min


if __name__ == '__main__':
    for key in ['iwrupvqb']:
        n, min = get_min(key)
        print(key)
        print(n)
        print(min)
        print()
