#!/usr/bin/env python

import unittest

import escape


class EscapeTest(unittest.TestCase):

    def test_escape_1(self):
        self.assertEqual(
                escape.escape('""'),
                r'"\"\""')

    def test_escape_2(self):
        self.assertEqual(
                escape.escape('"abc"'),
                r'"\"abc\""')

    def test_escape_3(self):
        self.assertEqual(
                escape.escape(r'"aaa\"aaa"'),
                r'"\"aaa\\\"aaa\""')

    def test_escape_4(self):
        self.assertEqual(
                escape.escape(r'"\x27"'),
                r'"\"\\x27\""')

class UnescapeTest(unittest.TestCase):

    def test_escape_1(self):
        self.assertEqual(
                escape.unescape('""'),
                '')

    def test_escape_2(self):
        self.assertEqual(
                escape.unescape('"abc"'),
                'abc')

    def test_escape_3(self):
        self.assertEqual(
                escape.unescape(r'"aaa\"aaa"'),
                r'aaa"aaa')

    def test_escape_4(self):
        self.assertEqual(
                escape.unescape(r'"\x27"'),
                "'")

