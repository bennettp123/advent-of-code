#!/usr/bin/env python

import unittest
import box


class Tester(unittest.TestCase):

    def test_box_area(self):
        w = 2
        h = 3
        l = 4
        area = box.box_area(w, h, l)
        self.assertEqual(area, 52)


    def test_smallest_side(self):
        w = 3
        h = 4
        l = 2
        smallest_side_area = box.smallest_side_area(w, l, h)
        self.assertEqual(smallest_side_area, 6)


    def test_paper_needed(self):
        w = 4
        h = 2
        l = 3
        expected = box.box_area(w, h, l) + box.smallest_side_area(h, l, w)
        actual = box.paper_needed(w, l, h)
        self.assertEqual(expected, actual)

