#!/usr/bin/env python


ids = set()
nodes = {}


class Node(object):

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

    def lookup_children(self):
        return [nodes[c] for c in self.children if c in nodes]

    def lookup_parents(self):
        return [nodes[c] for c in nodes if self.name in nodes[c].children]

    def __repr__(self):
        return 'Node(<{0}>: weight={1} children=[{2}])'.format(self.name, self.weight, ', '.join(self.children))


def add_prog(line):
    global graph
    global ids
    try:
        parent, children = line.split(' -> ')
        children = children.split(', ')
    except ValueError:
        parent = next(iter(line.split(' -> ')))
        children = []

    parent, weight = parent.split()
    weight = weight.strip('()')

    parent = parent.strip()
    children = [c.strip() for c in children]

    ids.add(parent)
    ids.update(children)

    nodes[parent] = Node(parent, weight, children)


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            add_prog(line)

    parents = [(k, v) for k, v in nodes.iteritems() if not v.lookup_parents()]

    for p in parents:
        print('part 1: parent found: {0}'.format(repr(p)))

