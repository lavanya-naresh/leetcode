# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/
'''
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n = n & (n - 1)
            result += 1
        return result