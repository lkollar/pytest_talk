#!/usr/bin/env python3 -m pytest tests/test_xfail.py
import pytest

@pytest.mark.xfail
def test_function():
    assert False
