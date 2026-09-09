# https://leetcode.com/problems/3sum/
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, 
nums[i] + nums[j] + nums[k] == 0

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                three_sum = a + nums[L] + nums[R]
                if three_sum > 0:
                    R -= 1
                elif three_sum < 0:
                    L += 1
                else:
                    result.append([a, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return result