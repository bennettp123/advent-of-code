#!/usr/bin/env python

if __name__ == '__main__':

    visited_locations = {}

    dirs = {"<": (-1, 0),
            ">": (1, 0),
            "^": (0, 1),
            "v": (0, -1)}

    pos = ["0 0", "0 0"]
    visited_locations["0 0"] = 2
    is_robosanta = 0

    with open('input', 'r') as f:
        for line in f:
            for char in line:
                is_robosanta = (is_robosanta + 1) % 2
                x, y = [int(x) for x in pos[is_robosanta].split()]
                try:
                    x_delta, y_delta = dirs[char]
                except KeyError:
                    # ignore whitespace, unicode BOMs, etc
                    continue
                pos[is_robosanta] = "{0} {1}".format(x + x_delta, y + y_delta)
                if pos[is_robosanta] not in visited_locations:
                    visited_locations[pos[is_robosanta]] = 0
                visited_locations[pos[is_robosanta]] += 1

    print('part2: {0} houses visited'.format(len(visited_locations)))

