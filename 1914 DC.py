# 1914. Cyclically Rotating a Grid
# https://leetcode.com/problems/cyclically-rotating-a-grid/description
'''
Given m * n integer matrix grid where both m and n are even and integer k.
The matrix is composed of layers. One cyclic rotation implies rotating each layer in the grid in the anti-clockwise direction by one element. 
Perform k cyclic rotations on grid and return the resulting grid.

Approach:
Identify layers in the grid and perform cyclic rotation for each layer.
'''
from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) / 2
        for layer in range(int(layers)):
            elements = []
            # top row
            for col in range(layer, n - layer):
                elements.append(grid[layer][col])
            # right column
            for row in range(layer + 1, m - layer):
                elements.append(grid[row][n - layer - 1])
            # bottom row
            for col in range(n - layer - 2, layer - 1, -1):
                elements.append(grid[m - layer - 1][col])
            # left column
            for row in range(m - layer - 2, layer, -1):
                elements.append(grid[row][layer])
            
            rotation = k % len(elements)
            rotated_elements = elements[rotation:] + elements[:rotation]
            
            index = 0
            # top row
            for col in range(layer, n - layer):
                grid[layer][col] = rotated_elements[index]
                index += 1
            # right column
            for row in range(layer + 1, m - layer):
                grid[row][n - layer - 1] = rotated_elements[index]
                index += 1
            # bottom row
            for col in range(n - layer - 2, layer - 1, -1):
                grid[m - layer - 1][col] = rotated_elements[index]
                index += 1
            # left column
            for row in range(m - layer - 2, layer, -1):
                grid[row][layer] = rotated_elements[index]
                index += 1        
        return grid