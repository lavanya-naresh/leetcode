# author = Lavanya Naresh
# created = Jan 7, 2023
# modified = Jan 7, 2023

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        delta = 0
        start = 0
        for index, (g, c) in enumerate(zip(gas, cost)):
            if tank < 0:
                start = index
                tank = 0
            tank += g - c
            delta += g - c
        return start if delta >= 0 else -1
