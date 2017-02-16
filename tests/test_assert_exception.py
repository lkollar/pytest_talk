#!/usr/bin/env python3 -m pytest tests/test_assert_exception.py

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# With custom error message
def test_zero_division():
    with pytest.raises(ZeroDivisionError, message="Exception thrown"):
        1 / 0
