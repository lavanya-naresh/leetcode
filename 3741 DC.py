from typing import List
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        INF = 10 ** 10
        N = len(nums)

        indices = defaultdict(list)

        for index, number in enumerate(nums):
            indices[number].append(index)

        result = INF
        for key in indices.keys():
            indices[key].sort()

            L = indices[key]
            for i, j, k in zip(L, L[1:], L[2:]):
                result = min(result, abs(i - j) + abs(j - k) + abs(i - k))

        return result if result != INF else -1