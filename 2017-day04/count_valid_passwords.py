#!/usr/bin/env python

import sys
import itertools


def permutations(string):
    permutations = [''.join(x) for x in itertools.permutations(string)]
    unique_permutations = set(permutations)
    return list(unique_permutations)


def all_anagrams(array):
    anagrams = []
    for word in array:
        anagrams = anagrams + permutations(word)
    return anagrams


def is_valid(array):
    anagrams = all_anagrams(array)
    return len(anagrams) == len(set(anagrams))


if __name__ == '__main__':
    passwords = (line for line in sys.stdin)
    valid_passwords = (p for p in passwords if is_valid(p.split()))
    count = 0
    for password in valid_passwords:
        count = count + 1
    print("Valid password count: {0}".format(count))


