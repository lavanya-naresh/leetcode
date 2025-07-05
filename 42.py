from typing import List
# tags:
# goldman sachs, 

# method 1: not optimized
class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxes = [0 for x in height]
        leftMax = 0
        
        for i in range(len(height)):
            maxes[i] = leftMax
            leftMax = max(leftMax, height[i])
            
        rightMax = 0
        for i in reversed(range(len(height))):
            minHeight = min(maxes[i], rightMax)
            if height[i] < minHeight:
                maxes[i] = minHeight - height[i]
            else:
                maxes[i] = 0
                
            rightMax = max(rightMax, height[i])
        
        return sum(maxes)
    
# method 2: optimized
# class Solution:
#     def trap(self, height: List[int]) -> int:
