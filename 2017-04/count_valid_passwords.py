#!/usr/bin/env python

import os
import sys


def is_unique(array):
    return len(array) == len(set(array))


if __name__ == '__main__':
    passwords = (line for line in sys.stdin)
    valid_passwords = (p for p in passwords if is_unique(p.split()))
    count = 0
    for password in valid_passwords:
        count = count + 1
    print("Valid password count: {0}".format(count))


