from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # nums = array of strings -> contains n unique binary strings each of length n
        # return binary string of length n that is not present in nums
        # if there are multiple answers return any of them
        # constraint: 1 <= n <= 16
        result_bits = []
        for i, w in enumerate(nums):
            result_bits.append(str(int(w[i]) ^ 1))
        return "".join(result_bits)
