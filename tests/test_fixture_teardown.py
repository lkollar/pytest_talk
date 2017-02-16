#!/usr/bin/env python3 -m pytest -s tests/test_fixture_teardown.py
import pytest
import queue

@pytest.fixture(scope="module", params=[2, 3, 100])
def queue_fixture(request):
    q = queue.Queue(request.param)
    yield q
    while not q.empty():
        q.get()
    print("queue empty")

def test_queue(queue_fixture):
    assert queue_fixture.empty()
    queue_fixture.put(10)
    queue_fixture.put(20)
    assert queue_fixture.get() == 10
