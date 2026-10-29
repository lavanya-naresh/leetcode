# https://leetcode.com/problems/valid-parentheses/description
class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep track of opening parentheses
        pStack = []
        pDict = {")": "(", "}": "{", "]": "["}

        for c in s:
            # add to stack if it is an opening parentheses
            if c in pDict.values():
                pStack.append(c)
                continue
            # check if it is a closing parentheses
            if c in pDict:
                # if opening stack is not empty, pop the last opening parentheses
                if len(pStack) != 0:
                    pOpen = pStack.pop()
                else:
                    return False

                # check if the popped opening parentheses matches the current closing parentheses
                if pOpen is not None and pDict[c] == pOpen:
                    continue
                else:
                    return False

        return len(pStack) == 0
