# author = Lavanya Naresh
# created = Jan 17, 2023
# modified = Jan 17, 2023

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        Approach:
        How to do brute force in a smart way? It is not always the case but one of the possible
        answers becomes visible with this approach.
        We will consider a partition.
        For a string of length N, we have N + 1 spaces.
        Example:
        | 0 | 1 | 1 |
        We take the number of zeroes on the right side of the partition and the number of ones on
        the left side. The minimum of the either will be the minimum possible from that partition.
        This partition will be moved from left to right and the best will be updated in each iteration.
        """
        N = len(s)
        result = N
        ones, ones_left = s.count("1"), 0
        zeroes = N - ones
        result = min(zeroes, result)

        for index in range(N):
            if s[index] == "1":
                # remove ones from right partition and add to left partition count
                ones -= 1
                ones_left += 1
            # update number of zeroes in the right partition and update result value in each iteration
            zeroes = N - index - 1 - ones
            result = min(result, zeroes + ones_left)
        return result
