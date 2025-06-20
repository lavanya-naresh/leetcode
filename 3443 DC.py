"""
3443. Maximum Manhattan Distance After K Changes
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:
    'N' : Move north by 1 unit.
    'S' : Move south by 1 unit.
    'E' : Move east by 1 unit.
    'W' : Move west by 1 unit.

Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

Example 1:
Input: s = "NWSE", k = 1
Output: 3
Explanation:
Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
"""
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dirs = [
            (0, 1), # N
            (1, 0), # E
            (0, -1), # S
            (-1, 0) # W
        ]

        ds = "NESW"
        counts = [0] * 4
        best = 0

        for c in s:
            d = ds.index(c)
            counts[d] += 1

            max_x = max(counts[1], counts[3])
            min_x = min(counts[1], counts[3])

            ck = k
            used = min(min_x, ck)
            min_x -= used
            ck -= used
            max_x += used            

            max_y = max(counts[0], counts[2])
            min_y = min(counts[0], counts[2])

            used = min(min_y, ck)
            min_y -= used
            ck -= used
            max_y += used

            best = max(best, max_x + max_y - min_x - min_y)

        return best