# author: Lavanya Naresh
# created: 3rd Jan, 2023
# last modified: 3rd Jan, 2023

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # bool flag list to indicate whether column should be removed or not     
        result = 0
        N, L = len(strs), len(strs[0])
        for col in range(L):
            for row in range(N):
                if row + 1 < N and strs[row][col] > strs[row + 1][col]:
                    result += 1
                    break
        return result
