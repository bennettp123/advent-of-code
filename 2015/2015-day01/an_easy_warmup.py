#!/usr/bin/env python

import sys

if __name__ == '__main__':

    floor = 0
    counter = 0
    with open('input', 'r') as f:
        for line in f:
            for char in line:
                counter = counter + 1
                if char == '(':
                    floor = floor + 1
                if char == ')':
                    floor = floor - 1
                if floor < 0:
                    print("on floor {0}, at counter {1}".format(floor, counter))
                    sys.exit(0)

