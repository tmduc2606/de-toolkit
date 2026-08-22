def passes_digit_checksum(record_id: int) -> bool:
    """Check whether an integer is divisible by its digit sum plus digit product.

    Original problem: LeetCode 3622 "Check Divisibility by Digit Sum and
    Product" — return True if n is divisible by the sum of its digits plus
    the product of its digits.

    DE use case: checksum-style validation of record IDs. A batch loader can
    recompute this divisibility property for numeric keys as a lightweight,
    dependency-free integrity gate before records enter the pipeline.

    Args:
        record_id: A positive integer (the LeetCode constraint is 1 <= n <= 100).

    Returns:
        True if record_id % (digit_sum + digit_product) == 0, else False.
    """
    # product default value must be 1
    # otherwise every value multiplied by 0 -> 0
    digit_sum = 0
    digit_prod = 1

    # Whether the integer is divisible by
    # the sum of digit_sum & digit_prod separated by given integer
    for digit in [int(d) for d in str(record_id)]:
        digit_sum += digit
        digit_prod *= digit

    if record_id % (digit_sum + digit_prod) == 0:
        return True
    else:
        return False


def valid_checksum_ids(record_ids):
    """Filter a batch of record IDs to those passing the digit checksum.

    DE use case: batch-level data-quality gate — keep only IDs whose digits
    satisfy the checksum before loading them downstream.

    Args:
        record_ids: An iterable of positive integers.

    Returns:
        A list containing only the IDs for which passes_digit_checksum is True.
    """
    return [rid for rid in record_ids if passes_digit_checksum(rid)]