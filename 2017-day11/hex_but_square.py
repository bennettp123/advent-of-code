#!/usr/bin/env python

x = 0
y = 0
maxd = 0

def move(x, y, d):
    directions = {'n': (0, 1), 'ne': (1, 1), 'se': (1, 0), 's': (0, -1),
            'sw': (-1, -1), 'nw': (-1, 0)}
    x_delta, y_delta = directions[d]
    return (x + x_delta, y + y_delta)


def shortest_distance_to_origin(pos):
    x, y = pos
    if x < 0 and y < 0: x, y = abs(x), abs(y)
    if x > 0 and y > 0: return max(x, y)
    else: return x + y


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            for d in line.split(','):
                x, y = move(x, y, d.strip())
                maxd = max(maxd, shortest_distance_to_origin((x, y)))

    print('part 1: shortest path to origin from {0}, {1} has distance {2}'
            .format(xpos, ypos, shortest_distance_to_origin((x, y))))

    print('part 2: maximum shortest path to origin had distance {0}'
            .format(maxd))

