import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_049 = importlib.import_module('049_group_anagrams_group_records')
mod_347 = importlib.import_module('347_top_k_frequent_elements_top_k_freq')
mod_692 = importlib.import_module('692_top_k_frequent_words_top_k_words')

group_records = mod_049.group_records
top_k_freq = mod_347.top_k_freq
top_k_words = mod_692.top_k_words


class TestGroupRecords:
    def test_group_anagrams(self):
        result = group_records(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
        groups = [set(g) for g in result]
        assert set(['eat', 'tea', 'ate']) in groups
        assert set(['tan', 'nat']) in groups
        assert set(['bat']) in groups

    def test_empty(self):
        assert group_records([]) == []

    def test_single_element(self):
        assert group_records(['abc']) == [['abc']]


class TestTopKFreq:
    def test_basic(self):
        result = top_k_freq([1, 1, 1, 2, 2, 3], 2)
        assert result == [1, 2]

    def test_k_equals_one(self):
        assert top_k_freq([1], 1) == [1]

    def test_all_same_frequency(self):
        result = top_k_freq([1, 2, 3], 2)
        assert len(result) == 2


class TestTopKWords:
    def test_basic(self):
        result = top_k_words(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2)
        assert result == ['i', 'love']

    def test_tie_breaker(self):
        result = top_k_words(['the', 'day', 'is', 'sunny', 'the', 'the', 'the', 'sunny', 'is', 'is'], 4)
        assert result == ['the', 'is', 'sunny', 'day']

    def test_single_word(self):
        assert top_k_words(['hello'], 1) == ['hello']