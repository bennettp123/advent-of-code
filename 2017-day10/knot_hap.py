#!/usr/bin/env python

import operator


def main():

    # part 1
    nums = range(256)
    pos = 0
    skip_size = 0
    lengths = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'.split(',')
    nums, pos, skip_size = round(nums, pos, skip_size, lengths)
    print('part 1: product of first two numbers is {0}'.format(nums[0]*nums[1]))

    # part 2
    nums = range(256)
    pos = 0
    skip_size = 0
    lengths = [ord(x) for x in '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'] + [17, 31, 73, 47, 23]
    for _ in range(64):
        nums, pos, skip_size = round(nums, pos, skip_size, lengths)

    sparse_hash = nums
    dense_hash = [reduce(operator.xor, sparse_hash[x:16+x])
                    for x in range(0, len(sparse_hash), 16)]

    hex_string = ''.join(['{:02x}'.format(int(c)) for c in dense_hash])
    print('part 2: hex string is {0}'.format(hex_string))


def round(nums, pos, skip_size, lengths):

    for length in (int(x) for x in lengths):

        forward_range = [(p % 256) for p in range(pos, pos+length)]
        reversed_nums = [nums[i] for i in reversed(forward_range)]

        for i in range(len(forward_range)):
            nums[forward_range[i]] = reversed_nums[i]

        pos += (length + skip_size) % len(nums)
        skip_size += 1

    return nums, pos, skip_size


if __name__ == '__main__':
    main()

