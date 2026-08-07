import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_026 = importlib.import_module('026_remove_duplicates_from_sorted_array_dedup_sorted')
mod_080 = importlib.import_module('080_remove_duplicates_from_sorted_array_ii_dedup_sorted_ii')

dedup_sorted = mod_026.dedup_sorted
dedup_sorted_ii = mod_080.dedup_sorted_ii


class TestDedupSorted:
    def test_basic(self):
        nums = [1, 1, 2]
        k = dedup_sorted(nums)
        assert k == 2
        assert nums[:k] == [1, 2]

    def test_all_unique(self):
        nums = [0, 1, 2, 3]
        k = dedup_sorted(nums)
        assert k == 4
        assert nums[:k] == [0, 1, 2, 3]

    def test_empty(self):
        nums = []
        k = dedup_sorted(nums)
        assert k == 0

    def test_single_element(self):
        nums = [1]
        k = dedup_sorted(nums)
        assert k == 1
        assert nums[:k] == [1]

    def test_all_duplicates(self):
        nums = [1, 1, 1]
        k = dedup_sorted(nums)
        assert k == 1
        assert nums[:k] == [1]


class TestDedupSortedII:
    def test_basic(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = dedup_sorted_ii(nums)
        assert k == 5
        assert nums[:k] == [1, 1, 2, 2, 3]

    def test_two_elements(self):
        nums = [1, 1]
        k = dedup_sorted_ii(nums)
        assert k == 2

    def test_empty(self):
        nums = []
        k = dedup_sorted_ii(nums)
        assert k == 0

    def test_all_unique(self):
        nums = [1, 2, 3]
        k = dedup_sorted_ii(nums)
        assert k == 3

    def test_many_duplicates(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        k = dedup_sorted_ii(nums)
        assert k == 7
        assert nums[:k] == [0, 0, 1, 1, 2, 3, 3]
