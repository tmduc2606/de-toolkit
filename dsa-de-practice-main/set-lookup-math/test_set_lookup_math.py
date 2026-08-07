import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_268 = importlib.import_module('268_missing_number_missing_single')
mod_448 = importlib.import_module('448_find_all_numbers_disappeared_missing_multi')

missing_single = mod_268.missing_single
missing_multi = mod_448.missing_multi


class TestMissingSingle:
    def test_missing_middle(self):
        assert missing_single([3, 0, 1]) == 2

    def test_missing_end(self):
        assert missing_single([0, 1]) == 2

    def test_missing_start(self):
        assert missing_single([1, 2]) == 0

    def test_single_element_zero(self):
        assert missing_single([0]) == 1


class TestMissingMulti:
    def test_basic(self):
        result = missing_multi([4, 3, 2, 7, 8, 2, 3, 1])
        assert sorted(result) == [5, 6]

    def test_no_missing(self):
        assert missing_multi([1, 2, 3]) == []

    def test_all_missing_except_one(self):
        result = missing_multi([2])
        assert result == [1]