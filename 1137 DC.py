# author = Lavanya Naresh
# created = Jan 30, 2023
# modified = Jan 30, 2023


class Solution:
    def tribonacci(self, n: int) -> int:
        # edge case n = 0, 1, 2
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        # DP solution
        result = [0] * n
        result[1] = result[2] = 1
        has_cache = [False] * n
        has_cache[0] = has_cache[1] = has_cache[2] = True

        def solver(x: int) -> int:
            res = 0
            if has_cache[x]:
                return result[x]
            for i in range(x):
                res = solver(x - 1) + solver(x - 2) + solver(x - 3)
            has_cache[x] = True
            result[x] = res
            return res

        solver(n)
        return result[-1]
