class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        N = len(word)
        firstCap = bool(ord(word[0]) in range(65, 91))
        allCaps, noCaps = [False] * N, [False] * N
        allCaps[0] = firstCap        
        noCaps[0] = not(firstCap)
        
        for idx, letter in enumerate(word):
            if ord(letter) in range(65, 91):
                allCaps[idx] = True
            else:
                noCaps[idx] = True
        
        if not all(noCaps):
            if any(noCaps):
                return firstCap and all(noCaps[1:])
            else: return all(allCaps)
        return all(noCaps)
