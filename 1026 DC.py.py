#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
File    :   1026 DC.py.py
Updated :   2024/01/11 20:47:38
Author  :   Lavanya Naresh 
Version :   1.0
Contact :   laksh112naresh@gmail.com
License :   (C)Copyright 2023-24, Lavanya Naresh
Desc    :   None
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        REQUIRED
        --------
        To find max value of v for which exist 2 diff nodes a and b, where:
        - v = abs(a.val - b.val)
        - a is ancestor of b or any child of a is ancestor of b

        CONSTRAINTS
        -----------
        - number of nodes in tree are in range [2, 5000]
        - 0 <= Node.val <= 10^5

        APPROACH
        --------
        To max the abs value of the diff b/w an ancestor and a node in their values.
        - abs(a.val - b.val)
        - difference can be taken using 2 end approach:
            - Track both the max value and the min value of ancestors and take the
            difference using the difference between node value from both max and min
        - update diff if current_diff > max_so_far

        """
        INF = 10**20
        result = 0

        def dfs(node, x, y):
            """
            Params
            ------
            node -> current node
            x -> max value of ancestors
            y -> min value of ancestors
            """
            # null check
            if node is None:
                return
            # use global variable and change scope of variable
            nonlocal result
            # update result if a greater difference is found
            result = max(result, x - node.val)
            result = max(result, node.val - y)
            # update the max and the min values of ancestors
            x, y = max(x, node.val), min(y, node.val)
            # DFS for left and right children of the node
            dfs(node.left, x, y)
            dfs(node.right, x, y)

        dfs(root, -INF, INF)
        return result
