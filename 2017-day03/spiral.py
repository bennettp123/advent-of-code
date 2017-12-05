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

    spiral = list(spiral_coords(312051))

    for coords in spiral:
        x, y = coords
        idx = idx + 1

    print("part1: distance is {0}".format(abs(x)+abs(y)))


