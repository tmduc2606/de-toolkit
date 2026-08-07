import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_217 = importlib.import_module('217_contains_duplicate_detect_duplicates')
mod_219 = importlib.import_module('219_contains_duplicate_ii_sliding_window_duplicates')

contains_duplicate = mod_217.contains_duplicate
sliding_window_duplicates = mod_219.sliding_window_duplicates


class TestContainsDuplicate:
    def test_has_duplicate(self):
        assert contains_duplicate([1, 2, 3, 1]) is True

    def test_no_duplicate(self):
        assert contains_duplicate([1, 2, 3]) is False

    def test_empty(self):
        assert contains_duplicate([]) is False

    def test_single_element(self):
        assert contains_duplicate([1]) is False

    def test_duplicate_at_end(self):
        assert contains_duplicate([1, 2, 3, 4, 1]) is True


class TestSlidingWindowDuplicates:
    def test_duplicate_within_window(self):
        assert sliding_window_duplicates([1, 0, 1, 2], 2) is True

    def test_duplicate_outside_window(self):
        assert sliding_window_duplicates([1, 2, 3, 1], 2) is False

    def test_duplicate_at_window_boundary(self):
        assert sliding_window_duplicates([1, 2, 3, 1], 3) is True

    def test_no_duplicates(self):
        assert sliding_window_duplicates([1, 2, 3, 4], 1) is False

    def test_empty(self):
        assert sliding_window_duplicates([], 0) is False