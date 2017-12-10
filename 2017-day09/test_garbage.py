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
    def testmethod(self):
        expected_startpos = 0
        expected_endpos = len(s) - 1
        actual_startpos, actual_endpos, _, _ = garbage.process(s)
        self.assertEqual(expected_startpos, actual_startpos)
        self.assertEqual(expected_endpos, actual_endpos)
    return testmethod


for n in range(len(garbage_strings)):
    s = garbage_strings[n]
    testmethod = get_testmethod(s)
    testmethod.__name__ = 'test_process_garbage_{0}'.format(n)
    setattr(GarbageTests, testmethod.__name__, testmethod)

for n in range(len(group_strings)):
    s = group_strings[n]
    testmethod = get_testmethod(s)
    testmethod.__name__ = 'test_process_group_{0}'.format(n)
    setattr(GroupTests, testmethod.__name__, testmethod)

groups_with_scores = [
        ('{}', 1),
        ('{{{}}}', 6),
        ('{{},{}}', 5),
        ('{{{},{},{{}}}}', 16),
        ('{<a>,<a>,<a>,<a>}', 1),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)]


def get_testmethod_with_score(s, expected_score):
    def testmethod(self):
        _, _, actual_score, _ = garbage.process(s)
        self.assertEqual(expected_score, actual_score)
    return testmethod


for n in range(len(groups_with_scores)):
    group, expected_score = groups_with_scores[n]
    testmethod = get_testmethod_with_score(group, expected_score)
    testmethod.__name__ = 'test_process_group_with_score_{0}'.format(n)
    setattr(GroupTests, testmethod.__name__, testmethod)


garbage_counts = [
        ('<>', 0),
        ('<random characters>', 17),
        ('<<<<>', 3),
        ('<{!>}>', 2),
        ('<!!>', 0),
        ('<!!!>>', 0),
        ('<{o"i!a,<{i<a>', 10),
        ('{<>}', 0),
        ('{<a>}', 1),
        ('{{{{<a>}}}}', 1),
        ('{{<{o"i!a,<{i<a>}}', 10)]


def get_testmethod_with_garbage_count(s, expected_garbage):
    def testmethod(self):
        _, _, _, actual_garbage = garbage.process(s)
        self.assertEqual(expected_garbage, actual_garbage)
    return testmethod


for n in range(len(garbage_counts)):
    s, expected_gargbage = garbage_counts[n]
    testmethod = get_testmethod_with_garbage_count(s, expected_gargbage)
    testmethod.__name__ = 'test_process_garbage_with_score_{0}'.format(n)
    setattr(GarbageTests, testmethod.__name__, testmethod)


if __name__ == '__main__':
    unittest.main()

