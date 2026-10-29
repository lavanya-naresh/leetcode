# https://leetcode.com/problems/longest-valid-parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        start = -1
        best = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i
                    continue
                stack.pop()
                if len(stack) > 0:
                    best = max(best, i - stack[-1])
                else:
                    best = max(best, i - start)
        return best


"""
)()())

stack = []
start = -1
best = 0
for
    i=0, c=)
        start = 0
        best = max(0, 0 - 0) = 0
    i=1, c=(
        stack = [1]
    i=2, c=)
        start = 0 (not updated)
        stack = []
        best = max(0, 2 - 0) = 2
    i=3, c=(
        stack = [3]
    i=4, c=)
        start = 0 (not updated)
        stack = []
        best = max(2, 4 - 0) = 4
    i=5, c=)
        start = 5 (updated because stack is empty ie. no opening parentheses to match)
        best = max(4, 5-5) = 4
return 4
"""
