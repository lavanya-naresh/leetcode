# https://leetcode.com/problems/trapping-rain-water/description
class Solution:
    def trap(self, height: list[int]) -> int:
        """
        water contained at position i = min(max height to the left of i, max height to the right of i) - height[i]
        """

        water = [0 for _ in range(len(height))]
        left_height, right_height = 0, 0

        for index in range(len(height)):
            water[index] = left_height
            left_height = max(left_height, height[index])

        for index in range(len(height) - 1, -1, -1):
            min_height = min(water[index], right_height)
            if min_height > height[index]:
                water[index] = min_height - height[index]
            else:
                water[index] = 0
            right_height = max(right_height, height[index])

        return sum(water)
