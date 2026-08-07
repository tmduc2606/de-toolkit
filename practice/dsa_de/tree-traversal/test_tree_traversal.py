import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

mod_094 = importlib.import_module('094_binary_tree_inorder_traversal_inorder')
mod_102 = importlib.import_module('102_binary_tree_level_order_traversal_level_order')
mod_104 = importlib.import_module('104_maximum_depth_of_binary_tree_max_depth')

inorder_traversal = mod_094.inorder_traversal
level_order_traversal = mod_102.level_order_traversal
max_depth = mod_104.max_depth
TreeNode = mod_104.TreeNode


class TestInorderTraversal:
    def test_empty_tree(self):
        assert inorder_traversal(None) == []

    def test_single_node(self):
        root = TreeNode(1)
        assert inorder_traversal(root) == [1]

    def test_full_bst(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        assert inorder_traversal(root) == [4, 2, 5, 1, 3]

    def test_left_skewed(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        assert inorder_traversal(root) == [1, 2, 3]

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert inorder_traversal(root) == [1, 2, 3]


class TestLevelOrderTraversal:
    def test_empty_tree(self):
        assert level_order_traversal(None) == []

    def test_single_node(self):
        root = TreeNode(1)
        assert level_order_traversal(root) == [[1]]

    def test_full_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        assert level_order_traversal(root) == [[3], [9, 20], [15, 7]]

    def test_left_skewed(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        assert level_order_traversal(root) == [[1], [2], [3]]

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert level_order_traversal(root) == [[1], [2], [3]]


class TestMaxDepth:
    def test_empty_tree(self):
        assert max_depth(None) == 0

    def test_single_node(self):
        root = TreeNode(1)
        assert max_depth(root) == 1

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        assert max_depth(root) == 3

    def test_left_skewed(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        assert max_depth(root) == 3

    def test_right_skewed(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert max_depth(root) == 3
