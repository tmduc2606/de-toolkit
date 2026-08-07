import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_215 = importlib.import_module('215_kth_largest_element_kth_largest')

kth_largest_element = mod_215.kth_largest_element


class TestKthLargestElement:
    def test_basic(self):
        assert kth_largest_element([3, 2, 1, 5, 6, 4], 2) == 5

    def test_single_element(self):
        assert kth_largest_element([1], 1) == 1

    def test_all_same(self):
        assert kth_largest_element([3, 3, 3, 3], 2) == 3

    def test_k_equals_one(self):
        assert kth_largest_element([1, 2, 3, 4, 5], 1) == 5

    def test_k_equals_length(self):
        assert kth_largest_element([1, 2, 3, 4, 5], 5) == 1

    def test_negative_numbers(self):
        assert kth_largest_element([-1, -2, -3, -4, -5], 2) == -2

    def test_unsorted_input(self):
        assert kth_largest_element([7, 10, 4, 3, 20, 15], 3) == 10