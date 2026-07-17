# 3312. Sorted GCD pair queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/description
# credit: https://www.youtube.com/@Algorithmist
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        INF = 10 ** 20
        nums.sort()

        """
        1  2, 3, 4 ... going up

        50000, 49999, ... , 1 

        220^2 -> all the factors

        """

        # factors[x] -> x appears as a factor for factors[x] count in nums
        factors = collections.Counter()
        for x in nums:
            current = 1
            while current * current <= x:
                if x % current == 0:
                    factors[current] += 1
                    if current * current != x:
                        factors[x // current] += 1
                current += 1

        mx = max(factors.keys())
        pairs = collections.Counter()
        # figure out the number of pairs
        for x in sorted(factors.keys(), reverse=True):
            pairs[x] = comb(factors[x], 2)
        
            current = x * 2
            while current <= mx:
                pairs[x] -= pairs[current]
                current += x

        prefix = [(0, -1)]
        for x in sorted(pairs.keys()):
            prefix.append((prefix[-1][0] + pairs[x], x))

        ans = []
        for q in queries:
            index = bisect.bisect_left(prefix, (q, INF))
            ans.append(prefix[index][1])
        return ans