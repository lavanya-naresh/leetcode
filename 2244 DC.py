# author = Lavanya Naresh
# created = Jan 4, 2023
# modified = Jan 4, 2023

from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        result = 0
        for count in freq.values():
            result += count // 3
            if count % 3 > 0:
                result += 1
            if count % 3 == 1 and count < 4:
                del freq
                return -1
        del freq
        return result
