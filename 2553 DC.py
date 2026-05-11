# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/description
'''
Given array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the order of their appearance in nums.
For integer value 10921 the separated digits would be [1,0,9,2,1].
'''
from typing import List
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for number in nums:
            for digit in str(number):
                ans.append(int(digit))
        return ans