# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = res[i - offset] + 1
        return res
