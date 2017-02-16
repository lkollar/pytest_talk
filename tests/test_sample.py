import pytest

@pytest.fixture
def thing():
    """Just a fixture returning True"""
    return True

def test_smoke(thing):
    assert thing
