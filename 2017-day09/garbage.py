#!/usr/bin/env python


backing = []


class Garbage(object):
    def __init__(self):
        self.val = None

    @staticmethod
    def is_selfcontained(s):
        if not s.startswith('<'):
            return False
        if not s.endswith('>'):
            return False
        if s.endswith('!>'):
            return False


class Group(object):
    def __init__(self):
        self.children = []
        self.val = None

    @staticmethod
    def is_selfcontained(s):
        if not s.startswith('{'):
            return False
        # TODO finish this

def next_thing(f):
    o = {}
    group = ''
    for line in f:
        for char in line:
            if garbage:
            else:
                if char = '{'
                    group += char
    # TODO finish this




if __name__ == '__main__':
    with open('input', 'r') as f:
        for o in next_thing(f):

