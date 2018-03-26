import pytest
from src import Store

def test_invalid_constructor_argument():
    with pytest.raises(Exception):
        Store(None)

