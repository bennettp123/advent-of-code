#!/usr/bin/env python

from graphlite import connect, V


if __name__ == '__main__':
    graph = connect(':memory:', graphs=['knows'])

    nums = []

    with open('input', 'r') as f:
        for line in f:
            src, dst = line.split(' <-> ')
            src = int(src)
            dst = [int(x) for x in dst.split(', ')]

            nums += [src]

            with graph.transaction() as tr:
                for d in dst:
                    tr.store(V(src).knows(d))
                    tr.store(V(d).knows(src))
                    nums += [d]

    nums = set(nums)

    query = graph.find(V(0).knows)
    groupsize = 0
    group = [0]

    if False:
        # disabled because it overflows the stack
        #
        # wtf -- how does an iterative
        # algorithm overflow the stack lol
        #
        while True:
            query = query.traverse(V().knows)
            group += [x for x in query]
            new_groupsize = len(set(group))
            if new_groupsize == groupsize:
                break
            groupsize = new_groupsize
    else:
        # recursive algorithm doesn't overflow the stack
        #
        # wtf lol
        #
        def friends_of(i):
            return [x for x in graph.find(V(i).knows)]

        def recursive_friends_of(i, visited=[]):
            myfriends = list(set(friends_of(i)))
            retval = [] + myfriends
            for friend in [recursive_friends_of(x, visited + [i])
                    for x in myfriends if not x in visited]:
                retval += friend
            return set(retval)

        groupsize = len(recursive_friends_of(0))

        print('part 1: node 0 group size is {0}'
                .format(groupsize))

        def lists_match(a, b):
            return set(a) == set(b)

        def list_in(a, l):
            return [x for x in l if lists_match(a, x)]

        unique_groups = []

        # this is probably O(n^6) or something
        for num in nums:
            group = recursive_friends_of(num)
            if not list_in(group, unique_groups):
                unique_groups += [group]

        # but it works
        print('part 2: found {0} unique groups'
                .format(len(unique_groups)))

