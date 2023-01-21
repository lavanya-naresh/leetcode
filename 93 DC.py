# author = Lavanya Naresh
# created = Jan 21, 2023
# modified = Jan 21, 2023

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        N = len(s)
        result = []

        def recurse(index, left, current):
            if left < 0:
                return
            
            if index == N:
                if left == 0:
                    result.append(".".join(current))
                return
            
            if s[index] == '0':
                current.append('0')
                recurse(index + 1, left - 1, current)
                current.pop()
                return
            
            for i in range(3):
                if index + i < N and 0 <= int(s[index: index + i + 1]) <= 255:
                    current.append(s[index: index + i + 1])
                    recurse(index + i + 1, left - 1, current)
                    current.pop()
            
        recurse(0, 4, [])
        return result
