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

    # Get a list of all nodes in the graph
    nodes = set(reduce(lambda x, y: x + [y[0], y[1]], edges, []))

    smallest_cost = sys.maxsize
    largest_cost = ~ sys.maxsize

    for path in itertools.permutations(nodes):

        possible = True
        min_path_cost = 0
        max_path_cost = 0

        for n1, n2 in pairwise(path):

            # 1. Assume these nodes are directly connected.

            # 2. Get the cost for these two directly connected nodes
            costs = [int(e[2]) for e in edges
                        if n1 in (e[0], e[1])
                        and n2 in (e[0], e[1])]

            # 3. If there is no cost for these nodes, then they are not
            #    directly connected. Ignore this path.
            if not len(costs):
                possible = False
                break

            min_path_cost += min(costs)
            max_path_cost += max(costs)

        if possible:
            smallest_cost = min(smallest_cost, min_path_cost)
            largest_cost = max(largest_cost, max_path_cost)

    print('part 1: shortest path through all nodes is {0}'
            .format(smallest_cost))

    print('part 2: longest path through all nodes is {0}'
            .format(largest_cost))

