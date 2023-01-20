# author = Lavanya Naresh
# created = Jan 10, 2023
# modified = Jan 10, 2023

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = set()
        def backtrack(indice, curr):
            if indice == len(nums):
                if len(curr) >= 2:
                    output.add(tuple(curr))
                return
            
            if not curr or curr[-1] <= nums[indice]:
                curr.append(nums[indice])
                backtrack(indice+1, curr)
                curr.pop()
            backtrack(indice+1, curr)
        
        backtrack(0, [])
        
        return output
