# author = Lavanya Naresh
# created = Jan 19, 2023
# modified = Jan 19, 2023

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        APPROACH:
        prefix sum
        
        Say we have an array:
           a0 a1 a2 a3 ... aN
        s0 s1 s2 s3 s4 ... s(N + 1)
        
        Assume:
        s5 - sX = k     ...(1)
        ie.
            (a0 + a1 + ... + a4)
        -   (a0 + a1 + ... + a(X - 1))
        ______________________________
        =   (a(X) + a(X + 1) + ... + a4) = k

        After rearranging the eqn (1), we have:
        s5 - k = sX     ...(2)

        Since the condition stipulated by the problem is divisibility by k, the conditions are:
            (s5 - sX) % k = 0           ...(1)
            (s5 % k) - (sX % k) = 0
        ->  s5 % k = sX % k             ...(2)
        """
        freq_subarr_sum = collections.Counter()
        freq_subarr_sum[0] = 1
        result = 0
        current = 0

        for x in nums:
            current += x
            current %= k
            result += freq_subarr_sum[current]
            freq_subarr_sum[current] += 1
        
        return result
