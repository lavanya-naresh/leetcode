"""
1391. Check if There is a Valid Path in a Grid
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

    1 which means a street connecting the left cell and the right cell.
    2 which means a street connecting the upper cell and the lower cell.
    3 which means a street connecting the left cell and the lower cell.
    4 which means a street connecting the right cell and the lower cell.
    5 which means a street connecting the left cell and the upper cell.
    6 which means a street connecting the right cell and the upper cell.
You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.
Notice that you are not allowed to change any street.
Return true if there is a valid path in the grid or false otherwise.

Approach: DFS
"""
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):
            if (row, col) == (m - 1, n - 1):
                return True
            visited[row][col] = True
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if new_row < 0 or new_row == m or new_col < 0 or new_col == n or visited[new_row][new_col]:
                    continue
                value = grid[row][col]
                if value == 1:
                    if ((new_col == col - 1 and grid[new_row][new_col] in (1, 4, 6)) or (new_col == col + 1 and grid[new_row][new_col] in (1, 3, 5))):
                        if dfs(new_row, new_col):
                            return True
                elif value == 2:
                    if ((new_row == row - 1 and grid[new_row][new_col] in (2, 3, 4)) or (new_row == row + 1 and grid[new_row][new_col] in (2, 5, 6))):
                        if dfs(new_row, new_col):
                            return True
                elif value == 3:
                    if ((new_col == col - 1 and grid[new_row][new_col] in (1, 4, 6)) or (new_row == row + 1 and grid[new_row][new_col] in (2, 5, 6))):
                        if dfs(new_row, new_col):
                            return True
                elif value == 4:
                    if ((new_col == col + 1 and grid[new_row][new_col] in (1, 3, 5)) or (new_row == row + 1 and grid[new_row][new_col] in (2, 5, 6))):
                        if dfs(new_row, new_col):
                            return True
                elif value == 5:
                    if ((new_col == col - 1 and grid[new_row][new_col] in (1, 4, 6)) or (new_row == row - 1 and grid[new_row][new_col] in (2, 3, 4))):
                        if dfs(new_row, new_col):
                            return True
                else:
                    if ((new_col == col + 1 and grid[new_row][new_col] in (1, 3, 5)) or (new_row == row - 1 and grid[new_row][new_col] in (2, 3, 4))):
                        if dfs(new_row, new_col):
                            return True                    
            return False
        return dfs(0, 0)