# author = Lavanya Naresh
# created = Jan 6, 2023
# modified = Jan 6, 2023

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return bisect_right(list(accumulate(sorted(costs))), coins)
        
# ALTERNATE:
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        N = len(costs)
        costs.sort()
        result = 0
        for c in costs:
            if coins >= c:
                coins -= c
                result += 1
        return result
