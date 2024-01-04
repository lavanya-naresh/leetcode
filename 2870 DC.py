from collections import Counter
from typing import List

#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
File    :   2870 DC.py
Updated :   2024/01/05 02:45:11
Author  :   Lavanya Naresh 
Version :   1.0
Contact :   laksh112naresh@gmail.com
License :   (C)Copyright 2023-24, Lavanya Naresh
Desc    :   None
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Objective: to find the min number of operations required to empty nums array

        Constraints:
        There are only 2 types of operations possible on nums array:
        1. 2 elements w equal values are selected and removed from nums
        2. 3 elements w equal values are selected and removed from nums

        Pattern:
        number of times -> min ops
        0 -> 0
        1 -> not possible -> -1
        2 -> 1 [2]
        3 -> 1 [3]
        4 -> 2 [2, 2]
        5 -> 2 [2, 3]
        6 -> 2 [3, 3]
        7 -> 3 [2, 2, 3]
        8 -> 3 [2, 3, 3]
        9 -> 3 [3, 3, 3]
        10 -> 4 [2, 2, 3, 3]
        ...

        As observed it follows the pattern of min number of ops reqd being equal
        for:
            F(3K - 2) = F(3K - 1) = F(3K) = K
        ->  min_ops = (freq + 2) // 3
        """

        f = Counter(nums)
        result = 0

        for v in f.values():
            if v == 1:
                return -1
            result += (v + 2) // 3

        return result
