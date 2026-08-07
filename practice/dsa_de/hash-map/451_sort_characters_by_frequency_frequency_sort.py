def frequency_sort(text):
    """Sort characters by their frequency in descending order.

    Uses a hash map to count frequencies, then sorts by count.

    In a data engineering context, this ranks items by occurrence
    frequency (e.g., sorting log levels by frequency, ordering
    categories by record count).

    Args:
        text: A string whose characters should be sorted by frequency.

    Returns:
        A string with characters sorted by descending frequency.
    """
    char_counts = {}
    for ch in text:
        char_counts[ch] = char_counts.get(ch, 0) + 1
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return ''.join(ch * count for ch, count in sorted_chars)