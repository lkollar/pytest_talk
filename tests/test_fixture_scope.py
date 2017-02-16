import pytest

@pytest.fixture(scope="module")
def queue_fixture(request):
    return queue.Queue(2)

def test_queue(queue_fixture):
    assert queue_fixture.empty()
    queue_fixture.put(10)
    queue_fixture.put(20)
    assert queue_fixture.get() == 10
