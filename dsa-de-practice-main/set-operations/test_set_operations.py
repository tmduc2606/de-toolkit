import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_349 = importlib.import_module('349_intersection_of_two_arrays_intersection_distinct')
mod_350 = importlib.import_module('350_intersection_of_two_arrays_ii_intersection_counts')

intersection_distinct = mod_349.intersection_distinct
intersection_counts = mod_350.intersection_counts


class TestIntersectionDistinct:
    def test_basic(self):
        assert sorted(intersection_distinct([1, 2, 2, 1], [2, 2])) == [2]

    def test_no_overlap(self):
        assert sorted(intersection_distinct([1, 2, 3], [4, 5, 6])) == []

    def test_full_overlap(self):
        assert sorted(intersection_distinct([1, 2, 3], [1, 2, 3])) == [1, 2, 3]

    def test_empty_first(self):
        assert sorted(intersection_distinct([], [1, 2])) == []

    def test_empty_second(self):
        assert sorted(intersection_distinct([1, 2], [])) == []

    def test_single_element(self):
        assert sorted(intersection_distinct([5], [5])) == [5]

    def test_duplicates_in_first(self):
        assert sorted(intersection_distinct([1, 1, 1, 2], [2, 3])) == [2]


class TestIntersectionCounts:
    def test_basic(self):
        assert sorted(intersection_counts([1, 2, 2, 1], [2, 2])) == [2, 2]

    def test_counts_respected(self):
        assert sorted(intersection_counts([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]

    def test_empty_first(self):
        assert intersection_counts([], [1, 2]) == []

    def test_no_overlap(self):
        assert intersection_counts([1, 2, 3], [4, 5]) == []

    def test_full_overlap(self):
        assert sorted(intersection_counts([1, 1, 2, 2], [1, 2, 1, 2])) == [1, 1, 2, 2]

    def test_single_element(self):
        assert intersection_counts([1], [1]) == [1]
