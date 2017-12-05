#!/usr/bin/env python

import sys

if __name__ == '__main__':

    part1_total = 0
    part2_total = 0
    array = []
    cur = None
    prev = None
    first = None

    with open('input', 'rb') as f:

        while True:

            char = f.read(1)
            if not char:
                # at EOF
                break

            try:
                cur = int(char)
            except ValueError:
                # ignore whitespace, unicode BOMs, alphabetic, etc
                continue

            # build an array
            array = array + [cur]

            if first is None:
                first = cur

            # caulculate part1_total
            if prev is not None:
                if prev == cur:
                    part1_total = part1_total + prev

            prev = cur

    # part1: handle wraparound
    if prev is not None:
        if first is not None:
            if first == cur:
                part1_total = part1_total + first

    # calculate part2_total
    offset = len(array) / 2
    for digit in range(0, len(array)):
        num = array[digit]
        if num == array[(digit + offset) % len(array)]:
            part2_total = part2_total + num

    print("part1 total is {0}".format(part1_total))
    print("part2 total is {0}".format(part2_total))

