def reverse_chars(s):
    """Reverse a string character by character.

    Uses a two-pointer swap approach, exchanging characters
    from both ends moving inward.

    DE reframing: reverse character order in a text field as a data transformation step.

    In a data engineering context, this reverses text fields
    in a dataset (e.g., reversing encoded values, mirroring
    string columns for transformation pipelines).

    Args:
        s: A list of characters to reverse in-place.

    Returns:
        None. s is modified in-place.
    """
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1