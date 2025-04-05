from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0

        def suffixXOR(index: int, current: int):
            if index == N:
                nonlocal result
                result += current
                return
            
            # CASE 1: include
            suffixXOR(index + 1, current ^ nums[index])

            # CASE 2: exclude
            suffixXOR(index + 1, current)

        suffixXOR(0, 0)
        return result