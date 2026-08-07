def dedup_sorted_ii(array):
    """Remove duplicates from a sorted array allowing at most two occurrences.

    DE reframing: remove excess duplicates from a sorted dataset, allowing at most two occurrences per value.

    In a data engineering context, this allows limited duplicates
    in a sorted dataset (e.g., keeping at most two entries per
    key in a sorted log, tolerating repeated sensor readings).

    Args:
        array: A sorted list of values.

    Returns:
        The length of the array after removing excess duplicates.
    """
    n, k = len(array), 2

    # Since the arr is sorted and atmost contains 2
    # duplicated values, immediate return cases of having
    # 2 values only
    if n <= 2:
        return n

    for i in range(2, len(array)):
        if array[i] != array[k - 2]:
            array[k] = array[i] # safe to copy, such that the previous num only have atmost 2
            k += 1

    return k
