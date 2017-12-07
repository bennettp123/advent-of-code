#!/usr/bin/env python

import re


def turn_on(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] = True
    return lights

def turn_off(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] = False
    return lights


def toggle(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] = not lights[row][col]
    return lights


if __name__ == '__main__':

    lights = [[False for row in range(1000)] for col in range(1000)]

    with open('input', 'r') as f:
        for line in f:
            op = re.match('(turn on|turn off|toggle)',
                    line).groups()[0]
            a, b, c, d = [int(x) for x in
                    re.search('(\d*),(\d*) through (\d*),(\d*)', line).groups()]
            if op == 'turn on':
                lights = turn_on(lights, a, b, c, d)
            elif op == 'turn off':
                lights = turn_off(lights, a, b, c, d)
            elif op == 'toggle':
                lights = toggle(lights, a, b, c, d)
            else:
                raise Exception('bad op! {0}'.format(op))

    num_lit = sum([lights[r].count(True) for r in range(1000)])

    print('part 1: {0} lights lit'.format(num_lit))

