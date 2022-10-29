# 2007 - Find Original Array From Doubled Array

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        N = len(changed)
        # check if the 
        if N % 2: return []
        result = []
        changed.sort()
        freq = collections.Counter()
        for value in changed:
            if value % 2 == 0 and value // 2 in freq and freq[value // 2] > 0:
                result.append(value // 2)
                freq[value // 2] -= 1
            else:
                freq[value] += 1
        if len(result) * 2 != len(changed): return []
        return result