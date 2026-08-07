import heapq


def kth_largest_element(elements, k):
    """Find the k-th largest element in a dataset using a min-heap.

    Maintains a min-heap of size k. For each element beyond the first k,
    if it is larger than the heap's minimum, it replaces it. The root
    of the heap is the k-th largest element.

    DE reframing: find the k-th largest value in a dataset using a heap-based
    priority queue, useful for top-k queries in streaming data.

    In a data engineering context, this identifies the k-th
    largest value in a stream or batch (e.g., the k-th highest
    revenue, the k-th most frequent event).

    Args:
        elements: A list of comparable elements.
        k: The rank position (1-indexed) to find.

    Returns:
        The k-th largest element.
    """
    heap = elements[:k]
    heapq.heapify(heap)

    for num in elements[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]