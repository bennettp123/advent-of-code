#!/usr/bin/env python


def box_area(w, h, l):
    return 2*w*h + 2*w*l + 2*h*l


def smallest_side_area(w, h, l):
    sides = (w*h, w*l, h*l)
    return min(sides)


def paper_needed(w, h, l):
    return box_area(w, h, l) + smallest_side_area(w, h, l)


def smallest_side_perimeter(w, l, h):
    sides = (2*(w+h), 2*(w+l), 2*(h+l))
    return min(sides)


def box_volume(w, l, h):
    return w * h * l


def ribbon_needed(w, l, h):
    return smallest_side_perimeter(w, l, h) + box_volume(w, l, h)


if __name__ == "__main__":

    total_paper = 0
    total_ribbon = 0

    with open('input', 'r') as f:

        for line in f:
            w, l, h = [int(x) for x in line.split('x')]
            total_paper = total_paper + paper_needed(w, h, l)
            total_ribbon = total_ribbon + ribbon_needed(w, l, h)


    print('total paper needed: {0}'.format(total_paper))
    print('total ribbon needed: {0}'.format(total_ribbon))


