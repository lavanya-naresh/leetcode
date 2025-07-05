class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f = Counter(arr)
        best = -1
        for k in f:
            if f[k] == k:
                best = max(best, k)
        return best