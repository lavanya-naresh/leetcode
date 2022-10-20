"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        res = []
        self.depth = {}
        maxDepth = self.dfs(root)
        for i in range(1, maxDepth + 1):
            res.append(self.depth.get(i))
        return res
    
    def dfs(self, node):
        if node is None: return 0
        d = max(self.dfs(node.left), self.dfs(node.right)) + 1
        if d not in self.depth:
            self.depth[d] = []
        self.depth[d].append(node.val)
        return d