#!/usr/bin/env python3 -m pytest tests/test_fixture.py

import queue
import pytest
@pytest.fixture()
def queue_fixture():
    return queue.Queue(2)

def test_queue(queue_fixture):
    assert queue_fixture.empty()
    queue_fixture.put(10)
    queue_fixture.put(20)
    assert queue_fixture.get() == 10
