#!/usr/bin/env python

import hashlib

def count():
    i = 0
    while True:
        yield i
        i += 1

if __name__ == '__main__':
    part1_found = False
    for num in count():
        digest = hashlib.md5('ckczppom{0}'.format(num)).hexdigest()
        if digest.startswith('000000'):
            print('part 2: num: {0} digest: {1}'.format(num, digest))
            break
        elif digest.startswith('00000') and not part1_found:
            print('part 1: num: {0} digest: {1}'.format(num, digest))
            part1_found = True
        elif num % 1000000 == 0:
            print('.')

