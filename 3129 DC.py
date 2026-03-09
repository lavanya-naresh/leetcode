# very poor problem description by the problem author
class Solution:
    def numberOfStableArrays(self, count_zero: int, count_one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        

        @cache
        def solve(zeros_rem: int, ones_rem: int, last_used: int) -> int:
            if zeros_rem == 0 and ones_rem == 0:
                return 1
            res = 0
            if last_used != 0:
                for streak in range(1, min(limit + 1, zeros_rem + 1)):
                    res += solve(zeros_rem - streak, ones_rem, 0)
            
            if last_used != 1:
                for streak in range(1, min(limit + 1, ones_rem + 1)):
                    res += solve(zeros_rem, ones_rem - streak, 1)
            
            return res % MOD
        
        result = solve(count_zero, count_one, -1)
        solve.cache_clear()
        return result