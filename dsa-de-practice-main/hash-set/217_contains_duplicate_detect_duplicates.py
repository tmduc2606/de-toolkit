def contains_duplicate(records):
    """Detect duplicate records in a dataset using a hash set.

    In a data engineering context, this identifies duplicate entries
    (e.g., duplicate order IDs, repeated user records) in a collection.

    Args:
        records: An iterable of hashable record identifiers.

    Returns:
        True if any duplicate exists, False otherwise.
    """
    seen = set()
    for record in records:
        if record in seen:
            return True
        seen.add(record)
    return False