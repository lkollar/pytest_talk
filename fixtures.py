
import smtplib

import pytest

from module import add_random_2


@pytest.fixture
def rand():
    def _(x, y):
        return 4
    return _


def test_random(rand):
    r = rand()
    assert add_random_2(r(0, 100), 4) == 8

def test_random_2(rand):
    r = rand()
    assert add_random_2(r(0, 100), 0) == 4
