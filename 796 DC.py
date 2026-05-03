class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        initial = [_ for _ in s]
        target = [_ for _ in goal]
        if initial == target:
            return True
        count = 0
        N = len(s)
        while count < N:
            first = initial.pop(0)
            initial.append(first)            
            if initial == target:
                return True
            count += 1
            
        return False