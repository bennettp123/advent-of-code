#!/usr/bin/env python


def box_area(w, h, l):
    return 2*w*h + 2*w*l + 2*h*l


def smallest_side_area(w, h, l):
    sides = (w*h, w*l, h*l)
    return min(sides)


def paper_needed(w, h, l):
    return box_area(w, h, l) + smallest_side_area(w, h, l)


if __name__ == "__main__":

    total_needed = 0

    with open('input', 'r') as f:

        for line in f:
            w, l, h = [int(x) for x in line.split('x')]
            total_needed = total_needed + paper_needed(w, h, l)

    print('total needed: {0}'.format(total_needed))


