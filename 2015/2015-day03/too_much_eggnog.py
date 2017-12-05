#!/usr/bin/env python

if __name__ == '__main__':

    visited_locations = {}

    dirs = {"<": (-1, 0),
            ">": (1, 0),
            "^": (0, 1),
            "v": (0, -1)}

    pos = "0 0"
    visited_locations[pos] = 1

    with open('input', 'r') as f:
        for line in f:
            for char in line:
                x, y = [int(x) for x in pos.split()]
                try:
                    x_delta, y_delta = dirs[char]
                except KeyError:
                    # ignore whitespace, unicode BOMs, etc
                    continue
                pos = "{0} {1}".format(x + x_delta, y + y_delta)
                if pos not in visited_locations:
                    visited_locations[pos] = 0
                visited_locations[pos] += 1

    print('part1: {0} houses visited'.format(len(visited_locations)))

