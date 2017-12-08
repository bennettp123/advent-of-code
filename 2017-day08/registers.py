#!/usr/bin/env python

import re
import sys

line_re = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+) (>=|>|<|<=|==|!=) (-?\d+)')

registers = {}
all_time_max = ~sys.maxsize


def process(line):
    global registers
    global all_time_max

    (target_reg, target_op, target_val,
            cond_reg, cond, cond_val) = line_re.match(line).groups()

    target_val = int(target_val)

    if target_op == 'dec':
        target_val = -target_val

    if not target_reg in registers:
        registers[target_reg] = 0

    if not cond_reg in registers:
        registers[cond_reg] = 0

    # bwahahahaha
    if eval('''int(registers['{0}']) {1} int({2})'''
                .format(cond_reg, cond, cond_val)):
        registers[target_reg] = registers[target_reg] + target_val
        all_time_max = max(all_time_max, registers[target_reg])


def main():
    with open('input', 'r') as f:
        for line in f:
            process(line)

    print('part 1: largest register has value {0}'
            .format(max((int(registers[x]) for x in registers))))

    print('part 2: all time max value had value {0}'
            .format(all_time_max))


if __name__ == "__main__":
    main()

