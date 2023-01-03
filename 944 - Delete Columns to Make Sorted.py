# author: Lavanya Naresh
# created: 3rd Jan, 2023
# last modified: 3rd Jan, 2023

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # bool flag list to indicate whether column should be removed or not
        col_to_remove = [0] * len(strs[0])
        N, L = len(strs), len(strs[0])
        for col in range(L):
            for row in range(N):
                if row + 1 < N and ord(strs[row][col]) > ord(strs[row + 1][col]):
                    col_to_remove[col] = 1
                    break
        return sum(col_to_remove) 
