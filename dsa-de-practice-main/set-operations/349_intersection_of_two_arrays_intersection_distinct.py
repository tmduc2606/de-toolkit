from collections import Counter

def intersection_distinct(arr1, arr2):
    """Find the intersection of two arrays with distinct results.

    DE reframing: find the set intersection of two datasets to identify common records.

    Uses set operations for O(1) membership checks.

    In a data engineering context, this finds common keys or
    identifiers between two datasets (e.g., overlapping user
    IDs between two tables, shared partition keys across datasets).

    Args:
        arr1: The first list of integers.
        arr2: The second list of integers.

    Returns:
        A list of distinct integers present in both arrays.
    """
    nums1_dict, nums2_dict = set(arr1), set(arr2)
    return list(nums1_dict.intersection(nums2_dict))
