import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_151 = importlib.import_module('151_reverse_words_in_string_reverse_order')
mod_344 = importlib.import_module('344_reverse_string_reverse_chars')
mod_125 = importlib.import_module('125_valid_palindrome_valid_palindrome')

reverse_words = mod_151.reverse_words
reverse_chars = mod_344.reverse_chars
valid_palindrome = mod_125.valid_palindrome


class TestReverseWords:
    def test_basic(self):
        assert reverse_words('the sky is blue') == 'blue is sky the'

    def test_single_word(self):
        assert reverse_words('hello') == 'hello'

    def test_leading_trailing_spaces(self):
        assert reverse_words('  hello world  ') == 'world hello'

    def test_multiple_spaces(self):
        assert reverse_words('a good   example') == 'example good a'

    def test_empty_string(self):
        assert reverse_words('') == ''

    def test_placeholder_docstring(self):
        assert 'DE reframing' in reverse_words.__doc__


class TestReverseChars:
    def test_basic(self):
        s = list('hello')
        reverse_chars(s)
        assert s == ['o', 'l', 'l', 'e', 'h']

    def test_single_char(self):
        s = list('a')
        reverse_chars(s)
        assert s == ['a']

    def test_empty(self):
        s = []
        reverse_chars(s)
        assert s == []

    def test_even_length(self):
        s = list('abcd')
        reverse_chars(s)
        assert s == ['d', 'c', 'b', 'a']

    def test_placeholder_docstring(self):
        assert 'DE reframing' in reverse_chars.__doc__


class TestValidPalindrome:
    def test_valid_palindrome(self):
        assert valid_palindrome('A man, a plan, a canal: Panama') is True

    def test_not_palindrome(self):
        assert valid_palindrome('race a car') is False

    def test_empty_string(self):
        assert valid_palindrome('') is True

    def test_single_char(self):
        assert valid_palindrome('a') is True

    def test_only_special_chars(self):
        assert valid_palindrome('.,') is True

    def test_placeholder_docstring(self):
        assert 'DE reframing' in valid_palindrome.__doc__