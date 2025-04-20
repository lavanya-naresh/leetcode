from typing import List
from collections import Counter 
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f = Counter(answers)
        result = 0

        for k in f.keys():
            # there are f[k] rabbits that observed k other rabbits as the same color
            # for each unique (k + 1) rabbits we have 1 group
            result += ((f[k] + k) // (k + 1)) * (k + 1)

        return result
