# 486. Predict the Winner
# https://leetcode.com/problems/predict-the-winner/description/
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            return max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))
        return dp(0, len(nums) - 1) >= 0