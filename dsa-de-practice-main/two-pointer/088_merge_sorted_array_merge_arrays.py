def merge_sorted_array(nums1, m, nums2, n):
    """Merge nums2 into nums1 in-place, where nums1 has enough space.

    Uses a three-pointer approach starting from the end of both arrays,
    filling nums1 from the back to avoid overwriting unprocessed elements.

    DE reframing: merge a sorted buffer into a pre-allocated sorted dataset in-place.

    In a data engineering context, this merges a sorted buffer
    into a larger sorted dataset (e.g., merging a sorted chunk
    into a pre-allocated partition, combining sorted segments
    in an external merge sort).

    Args:
        nums1: A list with m elements followed by n zeros (buffer space).
        m: The number of valid elements in nums1.
        nums2: A sorted list of n elements.
        n: The number of elements in nums2.

    Returns:
        None. nums1 is modified in-place to contain the merged result.
    """
    a, b, c = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if nums1[a] > nums2[b]:
            nums1[c] = nums1[a]
            a -= 1
        else:
            nums1[c] = nums2[b]
            b -= 1
        c -= 1

    while b >= 0:
        nums1[c] = nums2[b]
        c -= 1
        b -= 1

    return nums1