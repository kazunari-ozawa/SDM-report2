#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (999, calc(1,999))

        def test_sample3 (self):
                self.assertEqual (999, calc(999,1))

        def test_sample4 (self):
                self.assertEqual (-1, calc(5.66,28))

        def test_sample5 (self):
                self.assertEqual (-1, calc(0,31))

        def test_sample6 (self):
                self.assertEqual (-1, calc(-51,-41))

        def test_sample7 (self):
                self.assertEqual (-1, calc(1,1000))

        def test_sample8 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample9 (self):
                self.assertEqual (-1, calc(None,5))

