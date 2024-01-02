from collections import Counter
from typing import List

#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
File    :   2610 DC.py
Updated :   2024/01/02 20:47:21
Author  :   Lavanya Naresh 
Version :   1.0
Contact :   laksh112naresh@gmail.com
License :   (C)Copyright 2023-24, Lavanya Naresh
Desc    :   None
"""


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        # cond 1: result should contain only ints that are in nums array
        # cond 2: each row contains distinct ints
        # cond 3: minimize number of rows

        # minimum number of rows in result 2-D array = frequency of mode value in nums array
        frequencies = Counter(nums)
        rows = max(frequencies.values())
        result = []

        # iterator variables: current row iterates over result 2-D array, index over nums array
        current_row = 0
        index = 0
        added_in_result = [False] * N
        # iterate while the current row iterator does not exceed the max number of rows allowed
        while current_row < rows:
            result.append([])
            current_row_nums = set()
            # iterate over all numbers in nums
            for index in range(N):
                # if the number is already added to the result 2-D array, continue to next index
                if added_in_result[index]:
                    continue

                # if the number is not already in the current row
                if nums[index] not in current_row_nums:
                    current_row_nums.add(nums[index])
                    result[current_row].append(nums[index])
                    added_in_result[index] = True

            current_row += 1

        return result
