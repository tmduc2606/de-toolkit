def valid_palindrome(s):
    """Check if a string is a palindrome, ignoring non-alphanumeric characters and case.

    Uses two pointers from both ends, skipping non-alphanumeric
    characters, and compares characters case-insensitively.

    DE reframing: validate whether a text record reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    In a data engineering context, this validates data symmetry
    or checks for palindromic patterns in text fields (e.g.,
    validating symmetric identifiers, checking for palindromic
    sequences in genomic data).

    Args:
        s: A string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    i, j = 0, len(s) - 1

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True