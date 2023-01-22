# author = Lavanya Naresh
# created = Jan 23, 2023
# modified = Jan 23, 2023


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        result = []

        def helper(index: int, current: list):
            if index == N:
                result.append(current[:])
                return

            for i in range(index, N):
                c = s[index : i + 1]
                if c == c[::-1]:
                    current.append(c)
                    helper(i + 1, current)
                    current.pop()

        helper(index=0, current=[])
        return result
