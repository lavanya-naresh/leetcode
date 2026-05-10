# 2770. Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description
'''
Given array nums of length n and integer target.
Initial position is index 0.
You can jump from index i to any index j such that:
1) 0 <= i < j < n
2) -target <= nums[j] - nums[i] <= target in other words, abs(nums[j] - nums[i]) <= target
Return the max number of jumps you can make to reach index n - 1.
If there is no way to reach index n - 1, return -1.

Approach:
This problem can be solved using dynamic programming. The idea is to store the max number of jumps possible to reach each index in the array from the starting index.
For each index j, iterate over all previous indices i (where i < j) and check if the jump from index i to index j is valid (i.e., abs(nums[j] - nums[i]) <= target). If it is valid, update the max jumps for index j as the maximum of its current value and the max jumps for index i plus one (since we are making a jump from i to j).
'''
from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        # default for index 0 is 0
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        return dp[n - 1]