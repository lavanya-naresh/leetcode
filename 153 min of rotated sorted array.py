# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # pick the lower value from the first and last element as the initial result
        result = min(nums[0], nums[-1])
        L, R = 0, len(nums) - 1
        # iterate while the left pointer remains to the left of the right pointer
        while L < R:
            if nums[L] < nums[R]:
                result = min(result, nums[L])
                break

            # calculate the middle index and update the result with the min value found so far
            mid = (L + R) // 2
            result = min(result, nums[mid])

            # determine which part of the remaining search space should be searched next based on the comparison of middle value and the leftmost value
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid
        return result
