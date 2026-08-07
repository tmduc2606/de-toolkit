def pair_sum(transactions, target_amount):
    """Find two transactions whose amounts sum to a target value.

    Uses a hash map to store complement values for O(n) lookup.

    In a data engineering context, this identifies pairs of financial
    records that combine to a specific total (e.g., reconciling
    partial payments, finding offsetting entries).

    Args:
        transactions: A list of numeric transaction amounts.
        target_amount: The target sum to find.

    Returns:
        A list of two indices [i, j] such that transactions[i] + transactions[j] == target_amount,
        or an empty list if no such pair exists.
    """
    complement_map = {}
    for i, amount in enumerate(transactions):
        complement = target_amount - amount
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[amount] = i
    return []