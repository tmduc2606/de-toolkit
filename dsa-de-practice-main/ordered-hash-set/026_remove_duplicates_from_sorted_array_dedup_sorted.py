def dedup_sorted(array):
    """Remove duplicates from a sorted array in-place.

    DE reframing: remove duplicate records from a sorted dataset in-place.

    In a data engineering context, this deduplicates a sorted
    dataset (e.g., removing duplicate records from a sorted
    log file, collapsing repeated entries in an ordered list).

    Args:
        array: A sorted list of values.

    Returns:
        The length of the array after removing duplicates.
    """
    if not array:
        return 0

    count = 0

    # Compare the values in count, and i indices (0 & 1)
    # If both are identical, continue the iteration
    # If not, increment the count to swap between them
    # Continue to loop until all values are pushed

    for i in range(1, len(array)):
        if array[i] != array[count]:
            count += 1
            array[count] = array[i]

    return count + 1 # Python index mechanism
