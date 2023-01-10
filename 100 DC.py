# author = Lavanya Naresh
# created = Jan 10, 2023
# modified = Jan 10, 2023

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check_same(node1, node2) -> bool:
            if (not node1) != (not node2):
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            return check_same(node1.left, node2.left) and check_same(node1.right, node2.right)
        return check_same(p, q)
