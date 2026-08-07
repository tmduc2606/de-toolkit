import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_001 = importlib.import_module('001_two_sum_pair_sum')
mod_242 = importlib.import_module('242_valid_anagram_anagram_check')
mod_387 = importlib.import_module('387_first_unique_character_first_non_repeating')
mod_451 = importlib.import_module('451_sort_characters_by_frequency_frequency_sort')

pair_sum = mod_001.pair_sum
anagram_check = mod_242.anagram_check
first_non_repeating = mod_387.first_non_repeating
frequency_sort = mod_451.frequency_sort


class TestTwoSum:
    def test_basic(self):
        assert pair_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_no_solution(self):
        assert pair_sum([1, 2, 3], 10) == []

    def test_negative_numbers(self):
        assert pair_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


class TestAnagramCheck:
    def test_anagram(self):
        assert anagram_check('anagram', 'nagaram') is True

    def test_not_anagram(self):
        assert anagram_check('rat', 'car') is False

    def test_empty_strings(self):
        assert anagram_check('', '') is True

    def test_different_lengths(self):
        assert anagram_check('ab', 'a') is False


class TestFirstNonRepeating:
    def test_first_unique(self):
        assert first_non_repeating('leetcode') == 0

    def test_middle_unique(self):
        assert first_non_repeating('loveleetcode') == 2

    def test_no_unique(self):
        assert first_non_repeating('aabb') == -1


class TestFrequencySort:
    def test_basic(self):
        result = frequency_sort('tree')
        assert result == 'eert' or result == 'eetr'

    def test_single_char(self):
        assert frequency_sort('a') == 'a'

    def test_all_same(self):
        assert frequency_sort('aaaa') == 'aaaa'