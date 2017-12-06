#!/usr/bin/env python

def index_of_max(banks):
    biggest = 0
    for i in range(0, len(banks)):
        if banks[i] > banks[biggest]:
            biggest = i
    return biggest


def redistribute(banks):
    i = index_of_max(banks)
    num = banks[i]
    banks[i] = 0
    while num > 0:
        i = (i + 1) % len(banks)
        banks[i] += 1
        num -= 1
    return banks


def compare_lists(a, b):
    return hash(repr(a)) == hash(repr(b))


history = {}

def in_history(a):
    global history
    return hash(repr(a)) in history


def get_history(a):
    global history
    return history.get(hash(repr(a)))


def add_to_history(a, count=None):
    global history
    history.update({hash(repr(a)): count})


def clone_list(l):
    '''shallow clones a list to a new list'''
    return [x for x in l]


if __name__ == '__main__':

    banks = []

    with open('input', 'r') as f:
        for line in f:
            for bank in line.split():
                banks += [int(bank)]

    add_to_history(banks, 0)

    # do the first
    new_banks = clone_list(banks)
    new_banks = redistribute(new_banks)
    count = 1

    while not in_history(new_banks):
        add_to_history(new_banks, count)
        new_banks = redistribute(new_banks)
        count += 1

    print('part 1: redistributed {0} times'.format(count))
    print('part 2: first seen at {0} ({1} ago)'.format(get_history(new_banks), count-get_history(new_banks)))

