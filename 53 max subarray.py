class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, max_end = nums[0], nums[0]
        for index in range(1, len(nums)):
            number = nums[index]
            max_end = max(number, max_end + number)
            max_so_far = max(max_so_far, max_end)
        return max_so_far