#!/usr/bin/env python

import sys


def spiral_coords(size = sys.maxsize):
    '''returns a list of coords, spiralling around (0,0), relative to (0,0)'''

    index = 0
    x, y = (0, 0)

    distance = 0 # distance travelled in current direction
    max_distance = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 'right' => 'up' => 'left' => 'down'
    current_direction = 0

    while index < size:
        yield (x, y)

        # calculate the next coordinate
        x_delta, y_delta = directions[current_direction]
        x = x + x_delta
        y = y + y_delta

        distance = distance + 1
        if distance > max_distance:
            if current_direction in [1, 3]:
                max_distance = max_distance + 1
            distance = 0
            current_direction = (current_direction + 1) % 4

        index = index + 1


if __name__ == '__main__':
    idx = 0

    buf = [[None for i in range(0,1000)] for i in range(0,1000)]
    # origin = (500, 500)

    spiral = list(spiral_coords(312051))

    part2_found = False
    for coords in spiral:
        x, y = coords
        idx = idx + 1

        x1 = x + 500
        y1 = y + 500

        adjacent_coords = [ (x1 + 1, y1), (x1 + 1, y1 + 1),
                            (x1, y1 + 1), (x1 - 1, y1  + 1),
                            (x1 - 1, y1), (x1 - 1, y1 - 1),
                            (x1, y1 - 1), (x1 + 1, y1 - 1) ]

        adjacent_values = [buf[x][y] for x, y in adjacent_coords
                if not buf[x][y] is None]

        if not adjacent_values:
            buf[x1][y1] = 1
        else:
            buf[x1][y1] = sum(adjacent_values)

        if buf[x1][y1] > 312051:
            if not part2_found:
                print("part2: first sum greater than 312051 is {0}".format(
                    buf[x1][y1]))
                part2_found = True

    print("part1: distance is {0}".format(abs(x)+abs(y)))


