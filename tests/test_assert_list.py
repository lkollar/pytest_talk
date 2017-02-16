#!/usr/bin/env python3 -m pytest  tests/test_assert_list.py

def test_eq_list_long():
    a = [0]*100 + [1] + [3]*100
    b = [0]*100 + [2] + [3]*100
    assert a == b
