import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_341 = importlib.import_module('341_flatten_nested_list_iterator_flatten_nested')

NestedIterator = mod_341.NestedIterator


class TestFlattenNested:
    def test_nested_list(self):
        it = NestedIterator([[1, 1], 2, [1, 1]])
        result = []
        while it.has_next():
            result.append(it.next())
        assert result == [1, 1, 2, 1, 1]

    def test_deeply_nested(self):
        it = NestedIterator([1, [4, [6]]])
        result = []
        while it.has_next():
            result.append(it.next())
        assert result == [1, 4, 6]

    def test_single_element(self):
        it = NestedIterator([1])
        assert it.has_next() is True
        assert it.next() == 1
        assert it.has_next() is False

    def test_empty_list(self):
        it = NestedIterator([[]])
        assert it.has_next() is False