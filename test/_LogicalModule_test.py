import pytest
import src

def test_get_levenshtein():
    assert src.get_leveshtein("Iphone", "Iphone") == 0
    assert src.get_leveshtein("Iphone1", "Iphone") == 1
    assert src.get_leveshtein("" , "aaaaa") == 5
    assert src.get_leveshtein(None, None) == -1

def test_trim():
    assert src.trim("Iphone 7" , "Apple Iphone 7") == 0
    assert src.trim("Iphone 77" , "Apple Iphone 7") == 2
    assert src.trim(None , "lol") == -1
