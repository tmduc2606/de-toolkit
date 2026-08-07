def squares_sorted(nums):
    """Return the squares of a sorted array, also sorted.

    Uses a two-pointer approach starting from both ends,
    comparing absolute values and filling the result array
    from the back.

    DE reframing: compute squared values of a sorted numeric dataset and return them in sorted order.

    In a data engineering context, this transforms a sorted
    numeric dataset (which may contain negative values) into
    a sorted squared dataset (e.g., computing squared deviations
    from a baseline in order).

    Args:
        nums: A sorted list of integers.

    Returns:
        A sorted list of the squares of each number.
    """
    left, right, pos = 0, len(nums) - 1, len(nums) - 1
    result = [0] * len(nums)

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return result