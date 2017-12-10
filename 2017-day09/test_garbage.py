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

groups_with_scores = [
        ('{}', 1),
        ('{{{}}}', 6),
        ('{{},{}}', 5),
        ('{{{},{},{{}}}}', 16),
        ('{<a>,<a>,<a>,<a>}', 1),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)]


def get_testmethod(s):
    def test_process(self):
        expected_startpos = 0
        expected_endpos = len(s) - 1
        actual_startpos, actual_endpos, _ = garbage.process(s)
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


def get_testmethod_with_score(s, expected_score):
    def test_process(self):
        _, _, actual_score = garbage.process(s)
        self.assertEqual(expected_score, actual_score)
    return test_process


for n in range(len(groups_with_scores)):
    group, expected_score = groups_with_scores[n]
    test_method = get_testmethod_with_score(group, expected_score)
    test_method.__name__ = 'test_process_group_with_score_{0}'.format(n)
    setattr(GroupTests, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()

