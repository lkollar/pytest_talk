#!/usr/bin/env python3 -m pytest tests/test_assert_dict.py

def test_eq_dict():
    assert {'a': 0, 'b': 1, 'c': 0} == {'a': 0, 'b': 2, 'd': 0}

