from collections import Counter

def intersection_counts(arr1, arr2):
    """Find the intersection of two arrays with counts (multiset intersection).

    DE reframing: find the multiset intersection of two datasets, preserving occurrence counts.

    In a data engineering context, this finds common records
    between two datasets including their frequencies (e.g.,
    matching orders across two systems with quantity counts,
    finding overlapping events with occurrence counts).

    Args:
        arr1: The first list of integers.
        arr2: The second list of integers.

    Returns:
        A list of integers present in both arrays, with each
        element appearing as many times as it shows in both.
    """
    count = Counter(arr2)
    result = []

    # Idea: Since the intersection now also accepts duplicated values. It's safe to handle a dictionary on any lists
    # For safe counts, once the identical match is found, decrement the count of that value in dictionary.
    for num in arr1:
        if count[num] > 0:
            count[num] -= 1
            result.append(num)

    return result
