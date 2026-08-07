class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Perform in-order traversal of a binary tree.

    DE reframing: traverse a hierarchical data structure in sorted order for sequential processing.

    In a data engineering context, this traverses a hierarchical
    data structure in sorted order (e.g., extracting sorted
    keys from a BST index, walking a directory tree in order).

    Args:
        root: The root node of a binary tree.

    Returns:
        A list of node values in in-order sequence.
    """
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
