#!/usr/bin/env python

import re

strings = []


def vowels(s):
    return [c for c in s if c in ('a', 'e', 'i', 'o', 'u')]


def repeats(s):
    return re.search(r'(.)\1', s)


def blacklisted(s):
    return [b for b in ('ab', 'cd', 'pq', 'xy') if b in s]


def is_nice(s):
    return len(vowels(s)) > 2 and repeats(s) and not blacklisted(s)


def repeater(s):
    return re.search(r'(..).*\1', s)


def repleater(s):
    return re.search(r'(.).\1', s)


def is_nicer(s):
    return repeater(s) and repleater(s)


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            strings = strings + [line]

    nice_strings = [s for s in strings if is_nice(s)]
    nicer_strings = [s for s in strings if is_nicer(s)]

    print('part 1: {0} nice strings found'.format(len(nice_strings)))
    print('part 2: {0} nicer strings found'.format(len(nicer_strings)))

