import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_128 = importlib.import_module('128_longest_consecutive_sequence_longest_seq')

longest_consecutive_sequence = mod_128.longest_consecutive_sequence


class TestLongestConsecutiveSequence:
    def test_placeholder_raises(self):
        with pytest.raises(NotImplementedError):
            longest_consecutive_sequence([100, 4, 200, 1, 3, 2])

    def test_placeholder_docstring(self):
        assert 'DE reframing' in longest_consecutive_sequence.__doc__