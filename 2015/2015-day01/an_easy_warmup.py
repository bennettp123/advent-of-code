#!/usr/bin/env python

if __name__ == '__main__':

    floor = 0
    with open('input', 'r') as f:
        for line in f:
            ups = len([x for x in line if x == '('])
            downs = len([x for x in line if x == ')'])
            floor = floor + ups - downs

    print("on floor {0}".format(floor))

