import pytest
from pytest import approx

from module import add, div, add_random, DivError


# Simple assertions
def test_add():
    assert add(1, 2) == 3, "This is a failure"

# Expected failure
@pytest.mark.xfail
def test_add_fail():
    assert add(1, 2) == 4


# Floating point comparisons
@pytest.mark.xfail
def test_add_float():
    assert add(0.1, 0.2) == 0.3


def test_add_float_correct():
    assert add(0.1, 0.2) == approx(0.3)


def test_div():
    assert div(10, 5) == 2


# Assert exception is raised
def test_div_by_zero():
    with pytest.raises(DivError) as exc_info:
        assert div(10, 0) == 1
    assert exc_info.value.ERROR == 100


# Comparing complex types
@pytest.mark.xfail
def test_compare_complex():
    assert {1, 2, 4} == {1, 2, 3}


# FIXME
def test_add_random():
    assert add_random(10) > 0

import time
@pytest.mark.skip
@pytest.mark.parametrize("i", range(50))
def test_foobar(i):
    time.sleep(1)
    for x in range(i):
        assert i + x > 0



########## FIXTURES ###########
from module import Adder

@pytest.fixture(params=[0, 10, 20])
def adder_fixture(request):
    return (request.param, Adder(request.param))


def test_adder(adder_fixture):
    (expected, adder) = adder_fixture
    result = adder.add(10)
    assert result == expected + 10

#### SIMPLE
import queue

@pytest.fixture()
def queue_fixture():
    return queue.Queue(2)

def test_queue(queue_fixture):
    assert queue_fixture.empty()
    queue_fixture.put(10)
    queue_fixture.put(20)
    assert queue_fixture.get() == 10
    
@pytest.fixture(params=[2, 3, 100])
def queue_fixture_2(request):
    return queue.Queue(request.param)

def test_queue_2(queue_fixture_2):
    assert queue_fixture_2.empty()
    queue_fixture_2.put(10)
    queue_fixture_2.put(20)
    assert queue_fixture_2.get() == 10

@pytest.fixture(scope="module", params=[2, 3, 100])
def queue_fixture_3(request):
    return queue.Queue(request.param)

def test_queue_3(queue_fixture_3):
    assert queue_fixture_3.empty()
    queue_fixture_3.put(10)
    queue_fixture_3.put(20)
    assert queue_fixture_3.get() == 10

@pytest.fixture(scope="module", params=[2, 3, 100])
def queue_fixture_4(request):
    q = queue.Queue(request.param)
    yield q
    while not q.empty():
        q.get()

def test_queue_4(queue_fixture_4):
    assert queue_fixture_4.empty()
    queue_fixture_4.put(10)
    queue_fixture_4.put(20)
    assert queue_fixture_4.get() == 10


@pytest.mark.integration
def test_long_running():
    time.sleep(1)
    assert True
