#!/usr/bin/env python3 -m pytest tests/test_simple_pytest.py

def func(x):
    return x + 1

def test_func():
    assert func(3) == 5
