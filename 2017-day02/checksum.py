#!/usr/bin/env python


def part2_helper(vals):
    vals = sorted(vals)[::-1]
    for i in range(0, len(vals)):
        for j in range(i + 1, len(vals)):
            if vals[i] % vals[j] == 0:
                return vals[i] // vals[j]
    # default case is undefined


if __name__ == '__main__':

    part1_checksum = 0
    part2_checksum = 0

    with open('input', 'r') as f:
        for line in f:
            vals = [int(char) for char in line.split()]
            part1_checksum = part1_checksum + max(vals) - min(vals)
            part2_checksum = part2_checksum + part2_helper(vals)

    print('part1 checksum is {0}'.format(part1_checksum))
    print('part2 checksum is {0}'.format(part2_checksum))

