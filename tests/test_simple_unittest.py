#!/usr/bin/env python tests/test_simple_unittest.py

import pytest
import unittest

# Function under test
def func(x):
    return x + 1

# Unit test - Python unittest style
class TestClass(unittest.TestCase):
    def test_func(self):
        self.assertEqual(5, func(3))

if __name__ == '__main__':
    unittest.main()
