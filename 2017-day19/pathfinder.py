#!/usr/bin/env python


import re


lines = []
current_pos = None


def starting_pos(lines):
    '''given lines, returns x, y tuple of the starting position'''
    x = 0
    y = 0
    for line in lines:
        for char in line:
            if y == '|':
                return x, y
            y += 1
        x += 1


def is_obscured(lines, previous_pos, current_pos):
    '''given lines, previous position and current position, return True if the
    current position is obscured by another path'''


def next_pos(lines, previous_pos, current_pos):
    '''given lines, previous position and current position, determine the next
    position, or return None when at the end of the line'''
    x, y = current_pos
    prev_x, prev_y = previous_pos

    current_char = lines[x][y]

    if not current_pos:
        return starting_pos(lines)

    if re.match

    if is_obscured(lines, previous_pos, current_pos):
        # continue in the same direction
        x += (x - prev_x)
        y += (y - prev_y)
        return x, y

    if is_straight


with open('input', 'r') as f:
    for line in f:
        lines += [line]



import pdb; pdb.set_trace()

