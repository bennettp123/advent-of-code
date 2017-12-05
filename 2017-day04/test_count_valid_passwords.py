#!/usr/bin/env python

import unittest
import count_valid_passwords


class TestCountValidPasswordMethods(unittest.TestCase):


    def test_permutations_single(self):
        test_input = 'foo'
        expected = ['foo', 'ofo', 'oof']
        actual = count_valid_passwords.permutations(test_input)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(sorted(expected), sorted(actual))


    def test_permutations_empty(self):
        test_input = ''
        expected = ['']
        actual = count_valid_passwords.permutations(test_input)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(sorted(expected), sorted(actual))


    def test_all_anagrams_single(self):
        test_input = ['foo']
        expected = ['foo', 'ofo', 'oof']
        actual = count_valid_passwords.all_anagrams(test_input)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(sorted(expected), sorted(actual))


    def test_all_anagrams_multiple(self):
        test_input = ['foo', 'bar']
        expected = ['foo', 'ofo', 'oof', 'bar', 'bra', 'abr', 'arb', 'rab', 'rba']
        actual = count_valid_passwords.all_anagrams(test_input)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(sorted(expected), sorted(actual))


    def test_is_valid_single(self):
        test_input = 'foo'.split()
        self.assertTrue(count_valid_passwords.is_valid(test_input))


    def test_is_valid_multi_valid(self):
        test_input = 'foo bar baz'.split()
        self.assertTrue(count_valid_passwords.is_valid(test_input))


    def test_is_valid_multi_invalid(self):
        test_input = 'foo oof'.split()
        self.assertFalse(count_valid_passwords.is_valid(test_input))


if __name__ == '__main__':
    unittest.main()


