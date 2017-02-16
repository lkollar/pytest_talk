#!/usr/bin/env python3 -m pytest tests/test_assert_string.py

def test_eq_similar_text():
       assert 'foo 1 bar' == 'foo 2 bar'

