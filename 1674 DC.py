# 1674. Minimum Moves to Make Array Complementary
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/description
'''
GIVEN:
nums: integer array of length n
limit: integer

In 1 move you can replace any integer from nums with another integer between 1 and limit (inclusive).
The array nums is complementary if for all indices i:
nums[i] + nums[n - 1 - i] equals the same number.

APPROACH:

'''
from typing import List
from collections import Counter
from bisect import bisect_left
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        L = len(nums)
        l, r = 0, L - 1
        pairSums = Counter()
        lefts = []
        rights = []
        while l < r:
            pairSums[nums[l] + nums[r]] += 1
            lefts.append(min(nums[l], nums[r]))
            rights.append(max(nums[l], nums[r]))
            l += 1
            r -= 1
        lefts.sort(reverse = True)
        rights.sort()
        
        ans = int(1e10)
        for target in range(2, 2 * limit + 1):
            alreadyEqual = pairSums[target]
            sumTooHigh = bisect_left(lefts, 1 - target, key = lambda x: -x)
            sumTooLow = bisect_left(rights, target - limit)
            ans = min(L // 2 - alreadyEqual + sumTooHigh + sumTooLow, ans)
        return ans