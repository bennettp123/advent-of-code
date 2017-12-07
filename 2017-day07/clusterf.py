#!/usr/bin/env python


nodes = {}


class Node(object):

    def __init__(self, name, weight, child_names):
        self.name = name
        self.weight = int(weight)
        self.child_names = child_names

    def children(self):
        return [nodes[c] for c in self.child_names if c in nodes]

    def parents(self):
        return [nodes[c] for c in nodes if self.name in nodes[c].child_names]

    def is_balanced_shallow(self):
        return len(set([c.weight for c in self.children()])) < 2

    def is_balanced_deep(self):
        return len(set([c.tower_weight() for c in self.children()])) < 2

    def is_balanced(self):
        return self.is_balanced_deep()

    def tower_weight(self):
        return sum([c.tower_weight() for c in self.children()] + [self.weight])

    def __repr__(self):
        childstr = ''
        for child in self.child_names:
            childstr += '{0}({1}), '.format(nodes[child].name, nodes[child].tower_weight())
        childstr = childstr.rstrip(', ')
        return 'Node(<{0}>: weight={1} children=[{2}])'.format(self.name, self.weight, childstr)


def add_prog(line):
    global graph
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

    nodes[parent] = Node(parent, weight, children)


def parent_nodes():
    return [nodes[c] for c in nodes if not nodes[c].parents()]


def unbalanced_nodes():
    '''returns ALL unbalanced nodes'''
    nonleaves = (nodes[c] for c in nodes if nodes[c].child_names)
    return [n for n in nonleaves if not n.is_balanced()]


if __name__ == '__main__':
    with open('input', 'r') as f:
        for line in f:
            add_prog(line)

    for p in parent_nodes():
        print('part 1: parent found: {0}'.format(repr(p)))

    for node in unbalanced_nodes():
        print('part 2: unbalanced node found: {0}'.format(repr(node)))


    import pdb; pdb.set_trace()


