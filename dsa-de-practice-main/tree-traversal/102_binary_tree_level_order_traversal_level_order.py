from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    """Perform level-order (BFS) traversal of a binary tree.

    DE reframing: traverse a hierarchical data structure level by level for breadth-first processing.

    In a data engineering context, this processes hierarchical
    data level by level (e.g., processing organizational charts
    by tier, traversing nested JSON structures breadth-first).

    Args:
        root: The root node of a binary tree.

    Returns:
        A list of lists, where each inner list contains the
        node values at that level.
    """
    result, queue = [], deque([root])
    # BFS: Visits nodes level by level using a queue
    # Base case: Empty tree
    if root is None:
        return []

    while queue:
        # Add nodes with same level into []
        level = []

        for _ in range(len(queue)):
            # Root level
            current = queue.popleft()
            level.append(current.val)

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        # Once surfing the level, append to the result
        result.append(level)

    return result
