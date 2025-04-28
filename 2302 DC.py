from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def is_valid(left_index: int, right_index: int) -> bool:
            return (prefix[right_index + 1] - prefix[left_index]) * (right_index - left_index + 1) < k
        
        N = len(nums)

        prefix = [0]
        for x in prefix:
            prefix.append(x + prefix[-1])
        
        result = 0
        for i in range(N):
            if nums[i] >= k:
                continue

            L, R = i, N - 1
            while L < R:
                mid = (L + R + 1) // 2

                if is_valid(i, mid):
                    L = mid
                else:
                    R = mid - 1
            
            result += (R - i + 1)
        return result