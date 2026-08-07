import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_021 = importlib.import_module('021_merge_two_sorted_lists_merge_lists')
mod_088 = importlib.import_module('088_merge_sorted_array_merge_arrays')
mod_977 = importlib.import_module('977_squares_of_a_sorted_array_squares_sorted')

ListNode = mod_021.ListNode
merge_two_sorted_lists = mod_021.merge_two_sorted_lists
merge_sorted_array = mod_088.merge_sorted_array
squares_sorted = mod_977.squares_sorted


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def list_to_values(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


class TestMergeTwoSortedLists:
    def test_both_empty(self):
        assert merge_two_sorted_lists(None, None) is None

    def test_one_empty(self):
        l1 = build_list([1, 2, 4])
        assert list_to_values(merge_two_sorted_lists(l1, None)) == [1, 2, 4]

    def test_both_nonempty(self):
        l1 = build_list([1, 2, 4])
        l2 = build_list([1, 3, 4])
        assert list_to_values(merge_two_sorted_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]

    def test_single_element_each(self):
        l1 = build_list([1])
        l2 = build_list([2])
        assert list_to_values(merge_two_sorted_lists(l1, l2)) == [1, 2]


class TestMergeSortedArray:
    def test_basic(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        result = merge_sorted_array(nums1, 3, [2, 5, 6], 3)
        assert result == [1, 2, 2, 3, 5, 6]

    def test_nums1_empty(self):
        nums1 = [0, 0, 0]
        result = merge_sorted_array(nums1, 0, [1, 2, 3], 3)
        assert result == [1, 2, 3]

    def test_nums2_empty(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge_sorted_array(nums1, 3, [], 0)
        assert nums1[:3] == [1, 2, 3]

    def test_single_element_each(self):
        nums1 = [1, 0]
        result = merge_sorted_array(nums1, 1, [2], 1)
        assert result == [1, 2]

    def test_all_nums2_smaller(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        result = merge_sorted_array(nums1, 3, [1, 2, 3], 3)
        assert result == [1, 2, 3, 4, 5, 6]

    def test_placeholder_docstring(self):
        assert 'DE reframing' in merge_sorted_array.__doc__


class TestSquaresSorted:
    def test_basic(self):
        assert squares_sorted([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    def test_all_negative(self):
        assert squares_sorted([-7, -3, -1]) == [1, 9, 49]

    def test_all_positive(self):
        assert squares_sorted([1, 2, 3]) == [1, 4, 9]

    def test_single_element(self):
        assert squares_sorted([5]) == [25]

    def test_empty(self):
        assert squares_sorted([]) == []

    def test_mixed_with_zeros(self):
        assert squares_sorted([-2, 0, 2]) == [0, 4, 4]

    def test_placeholder_docstring(self):
        assert 'DE reframing' in squares_sorted.__doc__