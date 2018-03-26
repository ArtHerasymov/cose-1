import pytest
import src


def test_get_sites():
    assert src.get_sites('none.txt', "Iphone 7") is None
    assert len(src.get_sites('sites.xml', 'query')) == 4


def test_save_output():
    assert src.save_output('file.txt', None) is None
