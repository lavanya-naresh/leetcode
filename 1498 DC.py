from bisect import bisect_right
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        MOD = 1_000_000_000 + 7

        for idx, mi in enumerate(nums):
            ma = bisect_right(nums, target - mi) - 1
            if ma >= idx:
                ans += (1 << (ma - idx))
        return ans % MOD