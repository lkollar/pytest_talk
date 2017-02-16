#!/usr/bin/env python3 -m pytest tests/test_custom_markers.py

import pytest
import time

@pytest.mark.integration
def test_long_running():
    time.sleep(1)
    assert True

