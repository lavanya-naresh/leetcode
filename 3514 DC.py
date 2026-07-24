# 3514. Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/description
from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        duo_xor = set()
        for i in range(N):
            for j in range(i, N):
                duo_xor.add(nums[i] ^ nums[j])

        triplet_xor = set()
        for number in nums:
            for duo_xor_value in duo_xor:
                triplet_xor.add(number ^ duo_xor_value)

        return len(triplet_xor)