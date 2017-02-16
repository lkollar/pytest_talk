#!/usr/bin/env python3 -m pytest  tests/test_assert_set.py

def test_compare_complex():
   assert set([1,2,4]) == set([1,2,3])
