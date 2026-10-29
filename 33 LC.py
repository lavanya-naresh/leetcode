# https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
Since it is already mentioned in the problem statement that the required time complexity is O(log n)
The solution is to use binary search.
Vizualise the array as two sorted arrays, one on the left and one on the right where
all values in the left array are greater than all values in the right array.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[L] <= nums[mid]:  # left side is sorted
                if nums[L] <= target < nums[mid]:  # target is in the left side
                    R = mid - 1
                else:  # target is in the right side
                    L = mid + 1
            else:  # right side is sorted
                if nums[mid] < target <= nums[R]:  # target is in the right side
                    L = mid + 1
                else:  # target is in the left side
                    R = mid - 1
        return -1
