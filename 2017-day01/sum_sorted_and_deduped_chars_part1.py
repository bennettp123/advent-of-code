#!/usr/bin/env python

import sys

if __name__ == '__main__':

    total = 0
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

            if first is None:
                first = cur

            if prev is not None:
                if prev == cur:
                    total = total + prev

            prev = cur

    # handle wraparound
    if prev is not None:
        if first is not None:
            if first == cur:
                total = total + first

    print("total is {0}".format(total))

