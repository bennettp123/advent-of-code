#!/usr/bin/env python

import unittest

import garbage


class GarbageTests(unittest.TestCase):
    pass


class GroupTests(unittest.TestCase):
    pass


garbage_strings = [
        '<>',
        '<random characters>',
        '<<<<>',
        '<{!>}>',
        '<!!>',
        '<!!!>>',
        '<{o"i!a,<{i<a>']

group_strings = [
        '{}',
        '{{{}}}',
        '{{},{}}',
        '{{{},{},{{}}}}',
        '{<{},{},{{}}>}',
        '{<a>,<a>,<a>,<a>}',
        '{{<a>},{<a>},{<a>},{<a>}}',
        '{{<!>},{<!>},{<!>},{<a>}}']


def get_testmethod(s):
    def test_process(self):
        expected_startpos = 0
        expected_endpos = len(s) - 1
        actual_startpos, actual_endpos = garbage.process(s)
        self.assertEqual(expected_startpos, actual_startpos)
        self.assertEqual(expected_endpos, actual_endpos)
    return test_process


for n in range(len(garbage_strings)):
    s = garbage_strings[n]
    test_method = get_testmethod(s)
    test_method.__name__ = 'test_process_garbage_{0}'.format(n)
    setattr(GarbageTests, test_method.__name__, test_method)

for n in range(len(group_strings)):
    s = group_strings[n]
    test_method = get_testmethod(s)
    test_method.__name__ = 'test_process_group_{0}'.format(n)
    setattr(GroupTests, test_method.__name__, test_method)


if __name__ == '__main__':
    unittest.main()

