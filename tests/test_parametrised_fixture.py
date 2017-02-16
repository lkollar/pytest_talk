#!/usr/bin/env python3 -m pytest tests/test_parametrised_fixture.py
import pytest # OMIT
import queue # OMIT

@pytest.fixture(params=[2, 3, 100])
def queue_fixture(request):
    return queue.Queue(request.param)

def test_queue(queue_fixture):
    assert queue_fixture.empty()
    queue_fixture.put(10)
    queue_fixture.put(20)
    assert queue_fixture.get() == 10
