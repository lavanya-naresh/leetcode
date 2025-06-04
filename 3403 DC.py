class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1: return s
        return max(s[i:] for i in range(len(s)))[:len(s)-k+1]