#!/usr/bin/env python

import re


def turn_on(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] += 1
    return lights

def turn_off(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] = max(0, lights[row][col] - 1)
    return lights


def toggle(lights, a, b, c, d):
    for row in range(a, c+1):
        for col in range(b, d+1):
            lights[row][col] += 2
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

    sum_lit = sum([sum(lights[r]) for r in range(1000)])

    print('part 2: total brightness is {0}'.format(sum_lit))

