'''
Constraints:

    1 <= m, n <= 200
    0 <= k <= 10^3
    grid[0][0] == 0
    0 <= grid[i][j] <= 2

Top down DP problem
Memory limit exceeded exceeds if you simply write for 200 * 200 * 1000

Upon considering the problem, the max cost for given m, n is m + n (max = 400).
So creating the DP cache for 200 * 200 * 400 is feasible and does not exceed memory limits.

To further optimize for time, the iterations can be done over each row and column and create a 
defaultdict for each row in the grid that records the cost and the score for that row.
'''
from collections import defaultdict
from typing import List
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        row = [defaultdict(int, [(0, 0)])]

        for r in range(R):
            next_row = []
            for c in range(C):
                d = defaultdict(int)
                if c == 0 or r > 0:
                    for cost, score in row[c].items():
                        newcost = cost + (grid[r][c] > 0)
                        if newcost > k:
                            continue
                        newscore = score + grid[r][c]
                        d[newcost] = newscore
                if c > 0:
                    for cost, score in next_row[c - 1].items():
                        newcost = cost + (grid[r][c] > 0)
                        if newcost > k:
                            continue
                        newscore = score + grid[r][c]
                        d[newcost] = max(d[newcost], newscore)
                next_row.append(d)
            row = next_row

        return max(row[-1].values(), default=-1)