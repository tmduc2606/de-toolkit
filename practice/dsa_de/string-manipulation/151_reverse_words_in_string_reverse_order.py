def reverse_words(sentence):
    """Reverse the order of words in a string.

    Strips leading/trailing whitespace, splits on whitespace,
    reverses the word list, and rejoins with single spaces.

    DE reframing: reverse the order of fields/tokens in a text record.

    In a data engineering context, this reverses field order
    or token order in text records (e.g., reversing column
    order in a CSV row, reordering tokens in a log entry).

    Args:
        sentence: A string of words separated by spaces.

    Returns:
        A string with words in reverse order.
    """
    new_s = sentence.strip()
    return " ".join(new_s.split()[::-1])