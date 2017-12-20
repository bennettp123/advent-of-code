#!/usr/bin/env python

import knot_hap

my_prefix = 'ffayrhll'
test_prefix = 'flqrgnkx'

prefix = test_prefix


if __name__ == '__main__':

    sum_bits = 0

    for num in range(127):
        instr = '{0}-{1}'.format(prefix, num)
        knot_hash = knot_hap.knot_hash(instr)

        binary = bin(int(knot_hash, 16))[2:]

        sum_bits += sum([int(c) for c in bin(int('f2716f79f69efe9509e4e3f3c75035c9', 16))[2:]])

    print sum_bits
