# https://leetcode.com/problems/largest-rectangle-in-histogram/description


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        heights.append(0)
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(height * width, max_area)

            stack.append(i)
        heights.pop()
        return max_area
