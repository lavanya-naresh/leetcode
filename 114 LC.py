# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def traverse(node):
            if not node:
                return None
            left = self.traverse(node.left)
            right = self.traverse(node.right)

            node.left = None
            if left:
                node.right = left
                left_tail = get_right_tail(left)
                left_tail.right = right
            return node

        def get_right_tail(node):
            if not node or not node.right:
                return node
            return get_right_tail(node.right)

        return traverse(root)
