#!/usr/bin/env python3 -m pytest tests/monkeypatch_fail.py

import os

def test_cwd():
    assert os.getcwd() == '/'
