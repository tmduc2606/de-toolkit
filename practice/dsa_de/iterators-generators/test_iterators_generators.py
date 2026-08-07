import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_173 = importlib.import_module('173_binary_search_tree_iterator_bst_stream')
mod_284 = importlib.import_module('284_peeking_iterator_peek_stream')

BSTIterator = mod_173.BSTIterator
PeekingIterator = mod_284.PeekingIterator


class TestBSTIterator:
    def test_placeholder_raises(self):
        with pytest.raises(NotImplementedError):
            BSTIterator(None)

    def test_placeholder_docstring(self):
        assert 'DE reframing' in BSTIterator.__doc__


class TestPeekingIterator:
    def test_placeholder_raises(self):
        with pytest.raises(NotImplementedError):
            PeekingIterator(iter([1, 2, 3]))

    def test_placeholder_docstring(self):
        assert 'DE reframing' in PeekingIterator.__doc__