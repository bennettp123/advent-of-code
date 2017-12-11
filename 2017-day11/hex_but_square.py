#!/usr/bin/env python

xpos = 0
ypos = 0
maxdist = 0

def move(x, y, direction):
    directions = {'n': (0, 1), 'ne': (1, 1), 'se': (1, 0), 's': (0, -1),
            'sw': (-1, -1), 'nw': (-1, 0)}
    x_delta, y_delta = directions[direction]
    return (x + x_delta, y + y_delta)


def shortest_distance_to_origin(pos):
    x, y = pos
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return (min(abs(x), abs(y))
                 + max(abs(x), abs(y)) - min(abs(x), abs(y)))
    else:
        return x + y


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            for direction in line.split(','):
                xpos, ypos = move(xpos, ypos, direction.strip())
                maxdist = max(maxdist,
                        shortest_distance_to_origin((xpos, ypos)))

    print('part 1: shortest path to origin from {0}, {1} has distance {2}'
            .format(xpos, ypos, shortest_distance_to_origin((xpos, ypos))))

    print('part 2: maximum shortest path to origin had distance {0}'
            .format(maxdist))

