class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """Compute the maximum depth of a binary tree.

    Uses recursive DFS to find the longest path from root to leaf.

    DE reframing: determine the nesting depth of a hierarchical
    data structure (e.g., how many levels deep a JSON document
    goes, the depth of a category tree in a product catalog).

    Args:
        root: The root node of a binary tree.

    Returns:
        The maximum depth (number of nodes along the longest path
        from root to the farthest leaf node).
    """
    if root is None:
        return 0
    lheight = max_depth(root.left)
    rheight = max_depth(root.right)
    return max(lheight, rheight) + 1