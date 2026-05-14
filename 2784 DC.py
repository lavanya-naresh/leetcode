# 2784. Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/description
'''
GIVEN:
nums: integer array
Array is good if it is a permutation of an array base[n]
base[n] = [1, 2, 3, ..., n - 1, n, n]
'''
from typing import List
from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        f = Counter(nums)
        k = n - 1
        if f[k] != 2:
            return False
        for i in range(1, k):
            if f[i] != 1:
                return False
        return True