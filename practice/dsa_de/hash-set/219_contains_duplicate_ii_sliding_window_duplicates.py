def sliding_window_duplicates(events, window_size):
    """Check for duplicate events within a sliding window of given size.

    Uses a dict mapping event -> index to track positions, enabling
    O(1) lookup and index comparison for window-bound duplicate detection.

    In a data engineering context, this detects repeated events
    (e.g., duplicate log entries, repeated sensor readings) that
    occur within a configurable time or count window.

    Args:
        events: A list of event identifiers.
        window_size: Maximum distance (in indices) between two
            occurrences of the same event to count as a window duplicate.

    Returns:
        True if any duplicate event exists within the window, False otherwise.
    """
    index_map = {}
    for i, event in enumerate(events):
        if event in index_map and i - index_map[event] <= window_size:
            return True
        index_map[event] = i
    return False