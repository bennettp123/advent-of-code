#!/usr/bin/env python

import re
import sys
import itertools

edges = []


def pairwise(a):
    '''[1, 2, 3, 4, ..] => [(1, 2), (2, 3), (3, 4), ..]'''
    return zip(a[:-1], a[1:])


if __name__ == '__main__':

    regex = re.compile('(\w+) to (\w+) = (\d+)')

    with open('input', 'r') as f:
        for line in f:
            edges += [regex.match(line).groups()]

    nodes = set(reduce(lambda x, y: x + [y[0], y[1]], edges, []))

    smallest_cost = sys.maxsize

    for path in itertools.permutations(nodes):

        possible = True
        path_cost = 0

        for n1, n2 in pairwise(path):

            # get the shortest path between these two nodes
            costs = [int(e[2]) for e in edges
                        if n1 in (e[0], e[1])
                        and n2 in (e[0], e[1])]

            # ignore path unless node pairs are directly connected
            if not len(costs):
                possible = False
                break

            path_cost += min(costs)

        if possible:
            smallest_cost = min(smallest_cost, path_cost)

    print('part 1: shortest path through all nodes is {0}'
            .format(smallest_cost))

