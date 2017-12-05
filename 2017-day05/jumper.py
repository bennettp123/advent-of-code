#!/usr/bin/env python

if __name__ == '__main__':

    buf = []

    # slurp input
    with open('input', 'r') as f:
        for line in f:
            try:
                buf = buf + [int(line)]
            except ValueError:
                # ignore whitespace, unicode BOMs, etc
                pass

    pos = 0
    jumps = 0
    try:

        # jump around
        while True:
            target = pos + buf[pos]
            buf[pos] = buf[pos] + 1
            pos = target
            jumps = jumps + 1

    except IndexError:
        print('part1: jumped out of list in {0} jumps'.format(jumps))

