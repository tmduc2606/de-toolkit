def top_k_freq(elements, k):
    """Return the k most frequent elements in a dataset.

    Uses a hash map to count frequencies, then sorts by count.

    In a data engineering context, this identifies the top-k
    most common values in a dataset (e.g., top-k product IDs
    by sales count, most frequent error codes in logs).

    Args:
        elements: A list of hashable elements.
        k: The number of top frequent elements to return.

    Returns:
        A list of the k most frequent elements.
    """
    counts = {}
    for el in elements:
        counts[el] = counts.get(el, 0) + 1
    sorted_elements = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    return sorted_elements[:k]