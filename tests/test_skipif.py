import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,3),
                    reason="requires python3.3")
def test_function():
    pass
