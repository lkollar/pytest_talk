#!/usr/bin/env python3 -m pytest tests/monkeypatch_ok.py

import os

def silly_function():
    if os.getcwd() != '/':
        raise RuntimeError("I don't like you")
    else:
        return 'Kittens'

def test_cwd(monkeypatch):
    monkeypatch.setattr('os.getcwd', lambda: '/')
    assert silly_function() == 'Kittens'
