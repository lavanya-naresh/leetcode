# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        all_values = set(range(len(nums) + 1))
        for n in nums:
            all_values.discard(n)
        return all_values.pop()
