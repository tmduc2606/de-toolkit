def missing_multi(sequence):
    """Find all numbers in the range [1, n] that do not appear in the sequence.

    Uses a set for O(1) membership lookup to identify missing values.

    In a data engineering context, this finds all missing record IDs
    in a sequential dataset (e.g., gaps in a numbered log, missing
    partition keys in a distributed dataset).

    Args:
        sequence: A list of integers where each integer is in the range [1, n].

    Returns:
        A list of all integers in [1, n] that do not appear in sequence.
    """
    num_set = set(sequence)
    n = len(sequence)
    return [i for i in range(1, n + 1) if i not in num_set]