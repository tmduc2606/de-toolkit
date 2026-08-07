def first_non_repeating(stream):
    """Find the first non-repeating character in a data stream.

    Uses a hash map to count character frequencies, then scans
    for the first character with a count of 1.

    In a data engineering context, this identifies the first unique
    event in a stream (e.g., the first non-repeated log entry,
    the first distinct user action in a session).

    Args:
        stream: A string or iterable of characters/events.

    Returns:
        The index of the first non-repeating character, or -1 if none exists.
    """
    char_counts = {}
    for ch in stream:
        char_counts[ch] = char_counts.get(ch, 0) + 1
    for i, ch in enumerate(stream):
        if char_counts[ch] == 1:
            return i
    return -1