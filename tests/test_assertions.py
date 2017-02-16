#!/usr/bin/env python3 -m pytest tests/test_assertions.py

def add(x, y): # OMIT
    return x + y # OMIT
def test_simple_assert():
    assert add(1, 2) == 4

