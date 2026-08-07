def group_records(entries):
    """Group records that are anagrams of each other.

    Uses a hash map keyed by sorted character tuples to cluster
    anagram groups together.

    In a data engineering context, this groups related records
    that share the same composition but different ordering
    (e.g., grouping log entries by token set, clustering
    messages with the same word frequencies).

    Args:
        entries: A list of strings to group.

    Returns:
        A list of lists, where each inner list contains entries
        that are anagrams of each other.
    """
    groups = {}
    for entry in entries:
        key = tuple(sorted(entry))
        groups.setdefault(key, []).append(entry)
    return list(groups.values())