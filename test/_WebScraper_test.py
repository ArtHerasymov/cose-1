import src
import pytest


def test_valid_price_range():
    with pytest.raises(Exception):
        src.get_price_range(None, "Apple 7")
