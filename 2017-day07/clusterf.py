#!/usr/bin/env python


ids = set()
nodes = {}


class Node(object):

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = int(weight)
        self.children = children

    def lookup_children(self):
        return [nodes[c] for c in self.children if c in nodes]

    def lookup_parents(self):
        return [nodes[c] for c in nodes if self.name in nodes[c].children]

    def is_balanced_shallow(self):
        return len(set([c.weight for c in self.lookup_children()])) < 2

    def is_balanced_deep(self):
        return len(set([c.lookup_tower_weight() for c in self.lookup_children()])) < 2

    def is_balanced(self):
        return self.is_balanced_deep()

    def lookup_tower_weight(self):
        return sum([c.lookup_tower_weight() for c in self.lookup_children()] + [self.weight])

    def __repr__(self):
        childstr = ''
        for child in self.children:
            childstr += '{0}({1}), '.format(nodes[child].name, nodes[child].lookup_tower_weight())
        childstr = childstr.rstrip(', ')
        return 'Node(<{0}>: weight={1} children=[{2}])'.format(self.name, self.weight, childstr)


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


def unbalanced_nodes():
    '''returns ALL unbalanced nodes'''
    nonleaves = (nodes[c] for c in nodes if nodes[c].children)
    return [n for n in nonleaves if not n.is_balanced()]


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            add_prog(line)

    parents = [(k, v) for k, v in nodes.iteritems() if not v.lookup_parents()]

    for p in parents:
        print('part 1: parent found: {0}'.format(repr(p)))

    for node in unbalanced_nodes():
        print('part 2: unbalanced node found: {0}'.format(repr(node)))


    import pdb; pdb.set_trace()


