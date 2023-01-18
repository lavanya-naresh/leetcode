# author = Lavanya Naresh
# created = Jan 18, 2023
# modified = Jan 18, 2023


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        min_n = cur_n = inf
        max_x = cur_x = -inf
        total = 0
        for n in nums:
            cur_n = min(cur_n + n, n)
            min_n = min(min_n, cur_n)
            cur_x = max(cur_x + n, n)
            max_x = max(max_x, cur_x)
            total += n
        if total == min_n:
            return max_x
        return max(total - min_n, max_x)
