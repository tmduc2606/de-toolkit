class BSTIterator:
    """Iterates over a binary search tree in-order using a stack.

    DE reframing: provide an in-order iterator over a BST for streaming sorted records.

    In a data engineering context, this provides a streaming
    interface over sorted hierarchical data (e.g., iterating
    over sorted partition keys, streaming ordered records
    from a tree-indexed store).

    Args:
        root: The root node of a binary search tree.
    """

    def __init__(self, root):
        raise NotImplementedError("This problem has not yet been solved. "
                                  "DE reframing: provide an in-order iterator over a BST for streaming sorted records.")

    def next(self):
        raise NotImplementedError

    def has_next(self):
        raise NotImplementedError