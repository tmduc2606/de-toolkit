def top_k_words(documents, k):
    """Return the k most frequent words across documents.

    Uses a hash map to count word frequencies, then sorts by
    frequency (descending) and lexicographic order (ascending)
    for ties.

    In a data engineering context, this identifies the most
    common words in a text corpus (e.g., top-k keywords in
    support tickets, most frequent terms in log messages).

    Args:
        documents: A list of strings (documents or text entries).
        k: The number of top frequent words to return.

    Returns:
        A list of the k most frequent words, sorted by frequency
        descending, then lexicographically ascending for ties.
    """
    word_counts = {}
    for doc in documents:
        for word in doc.split():
            word_counts[word] = word_counts.get(word, 0) + 1
    sorted_words = sorted(word_counts.keys(), key=lambda w: (-word_counts[w], w))
    return sorted_words[:k]