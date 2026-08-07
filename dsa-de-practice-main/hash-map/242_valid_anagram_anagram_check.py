def anagram_check(source, target):
    """Check if two strings are anagrams by comparing character frequencies.

    Uses a hash map to count character occurrences in both strings.

    In a data engineering context, this validates whether two text
    records contain the same characters in different orders (e.g.,
    detecting reordered field values, comparing tokenized log entries).

    Args:
        source: The first string.
        target: The second string.

    Returns:
        True if source and target are anagrams, False otherwise.
    """
    if len(source) != len(target):
        return False
    char_counts = {}
    for ch in source:
        char_counts[ch] = char_counts.get(ch, 0) + 1
    for ch in target:
        char_counts[ch] = char_counts.get(ch, 0) - 1
        if char_counts[ch] < 0:
            return False
    return True