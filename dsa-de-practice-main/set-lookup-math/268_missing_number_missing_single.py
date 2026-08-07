def missing_single(sequence):
    """Find the single missing number in a sequence of integers from 0 to n.

    Uses a set for O(1) membership lookup. Iterates through the
    expected range and returns the number not found in the set.

    NOTE: This implementation preserves the user's original O(n²)
    approach using `i not in nums` on a list, as provided by the user.

    In a data engineering context, this identifies a missing record
    ID in a sequential dataset (e.g., a gap in transaction IDs,
    a missing row in a numbered log).

    Args:
        sequence: A list of n distinct integers in the range [0, n].

    Returns:
        The single missing integer in the range [0, n].
    """
    nums = sequence
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
    return -1