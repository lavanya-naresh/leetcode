# 2096. Step-By-Step Directions From a Binary Tree Node to Another
from typing import Optional
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
		
		start_node, end_node = None, None

		def dfs(node):
			# null node case
			if not node: return

			# if start or dest values are found
			if node.val == startValue:
				nonlocal start_node
				start_node = node
			if node.val == destValue:
				nonlocal end_node
				end_node = node
			
			# link left and right children of nodes with parent relationship to nodes
			if node.left is not None:
				node.left.parent = node
			if node.right is not None:
				node.right.parent = node
			
			dfs(node.left)
			dfs(node.right)
		
		root.parent = None
		dfs(root)

		q = collections.deque([start_node])
		previous = {}
		previous[start_node.val] = None

		# iterate until q is empty
		while len(q) > 0:
			current = q.popleft()

			if current.val == destValue:
				break

			if hasattr(current, 'parent') and current.parent is not None:
				if current.parent.val not in previous:
					previous[current.parent.val] = ("U", current.val)
					q.append(current.parent)

			if current.left is not None:
				if current.left.val not in previous:
					previous[current.left.val] = ("L", current.val)
					q.append(current.left)

			if current.right is not None:
				if current.right.val not in previous:
					previous[current.right.val] = ("R", current.val)
					q.append(current.right)

		current = destValue
		result = []
		while current in previous and previous[current] is not None:
			d, next_node = previous[current]
			result.append(previous[current][0])
			current = previous[current][1]

		return "".join(result[::-1])