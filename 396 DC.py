'''
Approach

Brute force will not work because O(n ^ 2) time complexity will lead to TLE.
To optimize we determine the relation between consecutive F(k) and F(k - 1) and use it to calculate F(k) from F(k - 1) in O(n) time.
The relation is as follows:

F(K) = F(K-1) + SUM(nums) - N * (nums[N - K])
'''
from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        best = 0
        total_sum = sum(nums)        
        f = sum([i * nums[i] for i in range(N)])
        best = f
        for k in range(1, N):
            f = f + total_sum - N * nums[N - k]
            best = max(best, f)        
        return best